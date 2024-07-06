from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryResult(BaseModel):
    queryText: str

class WebhookRequest(BaseModel):
    queryResult: QueryResult

@app.post("/webhook")
async def webhook(webhook_request: WebhookRequest):
    symptoms = webhook_request.queryResult.queryText
    # Here you can integrate your diagnosis model
    diagnosis = get_diagnosis(symptoms)
    response = {
        "fulfillmentText": f"จากอาการที่คุณระบุ {symptoms}, การวินิจฉัยเบื้องต้นคือ {diagnosis}"
    }
    return response

def get_diagnosis(symptoms):
    # Placeholder for actual diagnosis logic
    # Implement your model inference here
    diagnosis = "flu" if "ไข้" in symptoms else "migraine"
    return diagnosis
