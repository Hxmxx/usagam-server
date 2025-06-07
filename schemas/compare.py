from pydantic import BaseModel

class CompareRequest(BaseModel):
    sentence1: str
    sentence2: str