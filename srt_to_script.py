import re

def clean_dialogue(text):
    text = re.sub(r'\[.*?\]', '', text)
    # 특수문자 제거 (필요에 따라 수정)
    text = re.sub(r'[^\w\s가-힣]', '', text)
    # 공백 정리
    return ' '.join(text.split())

def extract_dialogues_from_srt(file_path):
    dialogues = []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r'\n\n+', content.strip())

    for block in blocks:
        lines = block.split('\n')

        if len(lines) >= 3:
            dialogue_lines = lines[2:]
            dialogue = ' '.join(dialogue_lines).strip()
            if dialogue:
                dialogues.append(dialogue)

    return dialogues

if __name__ == '__main__':
    file_path = "data/example.srt"
    dialogues = extract_dialogues_from_srt(file_path)
    dialogues = [clean_dialogue(d) for d in dialogues]

    for i, line in enumerate(dialogues[:10], 1):
        print(f"{i}: {line}")