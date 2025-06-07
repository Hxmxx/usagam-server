import random
from sentence_transformers import util

from infrastructure.vector_store import model, dialogues, titles
from infrastructure.user_store import save_user_sentence
from schemas import sentence


async def get_model_list():
    return [
        "snunlp/KR-SBERT-V40K-klueNLI-augSTS",
        "jhgan/ko-sbert-sts",
        "klue/roberta-base"
    ]

async def compare_sentences(sentence1: str, sentence2: str):
    vec1 = model.encode([sentence1], convert_to_tensor=True)
    vec2 = model.encode([sentence2], convert_to_tensor=True)
    sim = float(util.cos_sim(vec1, vec2)[0][0])
    return {"similarity": f"{sim * 100:.2f}%"}

async def get_random_sentence():
    idx = random.randint(0, len(dialogues) - 1)
    return {
        "title": titles[idx],
        "sentence": dialogues[idx],
    }

async def store_user_sentence(title: str, sentence: str):
    save_user_sentence(title, sentence)
    return {"message": "대사가 저장되었습니다."}

async def health_check():
    return {"status": "ok"}