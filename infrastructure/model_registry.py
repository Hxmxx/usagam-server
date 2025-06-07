from functools import lru_cache
from sentence_transformers import SentenceTransformer

@lru_cache()
def get_model(model_name: str = "snunlp/KR-SBERT-V40K-klueNLI-augSTS") -> SentenceTransformer:
    print(f"Loading {model_name} model...")
    return SentenceTransformer(model_name)