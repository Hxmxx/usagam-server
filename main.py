import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util
import json

from data_preprocessing import preprocess_korean

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
max_result = 7

model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
# model = SentenceTransformer('jhgan/ko-sbert-sts')

with open("data/sentences.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

titles = []
dialogues = []
for item in raw_data:
    for title, line in item.items():
        titles.append(title)
        dialogues.append(line)

sentences_embedding = model.encode(dialogues, convert_to_tensor=True)

class SentenceRequest(BaseModel):
    sentence: str

@app.post("/predict")
def get_similar_sentences(request: SentenceRequest):
    processed = preprocess_korean(request.sentence)
    query_embedding = model.encode([processed], convert_to_tensor=True)

    cos_scores = util.cos_sim(query_embedding, sentences_embedding)[0]

    top_result = cos_scores.argsort(descending=True)[:max_result]

    results = []

    for idx in top_result:
        results.append({
            "title": titles[idx],
            "sentence": dialogues[idx],
            "score": float(cos_scores[idx])
        })

    return {
        "input": request.sentence,
        "output": results
    }

@app.get("/get_predict")
def get_sentences_json():
    return raw_data

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)