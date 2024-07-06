from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf
from app.core.config import settings

model = TFAutoModelForSequenceClassification.from_pretrained(settings.MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_NAME)

def get_diagnosis(symptoms):
    inputs = tokenizer(symptoms, return_tensors="tf")
    outputs = model(inputs)
    predictions = tf.nn.softmax(outputs.logits, axis=-1)
    diagnosis = "flu" if tf.argmax(predictions, axis=1).numpy()[0] == 0 else "migraine"
    return diagnosis
