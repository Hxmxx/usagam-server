import json
from sentence_transformers import util
from domain.repository import SentenceRepository

from infrastructure.model_registry import get_model

with open("data/sentences.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

titles, dialogues = [], []
for item in raw_data:
    for title, line in item.items():
        titles.append(title)
        dialogues.append(line)

model = get_model()
embeddings = model.encode(dialogues, convert_to_tensor=True)

class SentenceVectorStore(SentenceRepository):
    def find_similar(self, input_sentence: str):
        query = model.encode([input_sentence], convert_to_tensor=True)
        scores = util.cos_sim(query, embeddings)[0]
        top_k = scores.argsort(descending=True)[:3]

        return [
            {
                "title": titles[i],
                "sentence": dialogues[i],
                "score": f"{scores[i].item() * 100:.1f}% "
            }
            for i in top_k
        ]

vector_store = SentenceVectorStore()