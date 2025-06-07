from fastapi import APIRouter
from schemas.sentence import SentenceRequest
from application.service import predict_similar_sentences

router = APIRouter()

@router.post("/predict")
async def predict(request: SentenceRequest):
    return await predict_similar_sentences(request.sentence)

@router.get("/get_predict")
async def get_raw_data():
    from infrastructure.vector_store import raw_data
    return await raw_data