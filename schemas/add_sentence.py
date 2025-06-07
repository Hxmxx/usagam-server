from pydantic import BaseModel

class AddSentenceRequest(BaseModel):
    title: str
    sentence: str