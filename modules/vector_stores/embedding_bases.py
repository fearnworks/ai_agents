from abc import ABC, abstractmethod        
class DocumentLoadStrategy(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def split(self, documents, chunk_size, chunk_overlap):
        pass 