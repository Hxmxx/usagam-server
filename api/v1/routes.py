from fastapi import APIRouter
from schemas.sentence import SentenceRequest
from schemas.compare import CompareRequest
from schemas.add_sentence import AddSentenceRequest
from application.service import predict_similar_sentences
from application.misc_service import (
    compare_sentences, get_model_list, get_random_sentence,
    store_user_sentence, health_check
)

router = APIRouter()

@router.post("/predict")
async def predict(request: SentenceRequest):
    return await predict_similar_sentences(request.sentence)

@router.get("/get_predict")
async def get_raw_data():
    from infrastructure.vector_store import raw_data
    return raw_data

@router.post("/compare")
async def compare(request: CompareRequest):
    return await compare_sentences(request.sentence1, request.sentence2)

@router.get("/models")
async def models():
    return await get_model_list()

@router.get("/random")
async def random_sentence():
    return await get_random_sentence()

@router.post("/add-sentence")
async def add_sentence(req: AddSentenceRequest):
    return await store_user_sentence(req.title, req.sentence)

@router.get("/health")
async def health():
    return await health_check()