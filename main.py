from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.calibration import LabelEncoder
import tensorflow as tf
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('covid_diagnosis_model.h5')

# Load the label encoder
le = LabelEncoder()
le.fit(['COVID-19', 'Flu', 'Common Cold'])

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class Symptoms(BaseModel):
    fever: int
    cough: int
    fatigue: int
    sore_throat: int
    shortness_of_breath: int
    headache: int

@app.post('/predict')
def predict(symptoms: Symptoms):
    try:
        input_data = np.array([[
            symptoms.fever, symptoms.cough, symptoms.fatigue,
            symptoms.sore_throat, symptoms.shortness_of_breath, symptoms.headache
        ]])
        predictions = model.predict(input_data)
        predicted_class = le.inverse_transform([np.argmax(predictions)])
        return {'diagnosis': predicted_class[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
