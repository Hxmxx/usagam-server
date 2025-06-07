import json

def save_user_sentence(title: str, sentence: str, path="data/user_sentences.jsonl"):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps({title: sentence}, ensure_ascii=False) + "\n")
