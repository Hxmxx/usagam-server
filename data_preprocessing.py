import re, os

def load_stopwords(path='data/korean_stop_words.txt'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"불용어 파일이 '{path}' 경로에 존재하지 않습니다.")
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def preprocess_korean(text: str) -> str:
    text = re.sub(r"[^가-힣\s]", "", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

stop_words = load_stopwords()