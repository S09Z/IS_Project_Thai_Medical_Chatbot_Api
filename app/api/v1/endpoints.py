from fastapi import APIRouter
from pydantic import BaseModel
from app.models.diagnosis_model import get_diagnosis

router = APIRouter()

class QueryResult(BaseModel):
    queryText: str

class WebhookRequest(BaseModel):
    queryResult: QueryResult

@router.post("/webhook")
async def webhook(webhook_request: WebhookRequest):
    symptoms = webhook_request.queryResult.queryText
    diagnosis = get_diagnosis(symptoms)
    response = {
        "fulfillmentText": f"จากอาการที่คุณระบุ {symptoms}, การวินิจฉัยเบื้องต้นคือ {diagnosis}"
    }
    return response
