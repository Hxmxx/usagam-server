from fastapi import HTTPException
import logging

async def predict_similar_sentences(input_sentence: str):
    from utils.data_preprocessing import preprocess_korean
    from infrastructure.vector_store import vector_store

    try:
        if not input_sentence or input_sentence == "" or input_sentence == " ":
            raise ValueError("입력 문장이 비어 있습니다.")

        processed = preprocess_korean(input_sentence)
        result = vector_store.find_similar(processed)

        return {
            "success": True,
            "input": input_sentence,
            "output": result,
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        logging.exception("예측 중 오류 발생")
        raise HTTPException(status_code=500, detail="서버 오류가 발생했습니다.")