from abc import ABC, abstractmethod
from typing import List

class SentenceRepository(ABC):
    @abstractmethod
    async def find_similar(self, input_sentence: str) -> List[dict]:
        pass