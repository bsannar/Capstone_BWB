from abc import ABC, abstractmethod

class InternalStorageInterface(ABC):
    @abstractmethod
    def pull_from_dict(self, dictionary: dict):
        pass

    @abstractmethod
    def push_to_dict(self) -> dict:
        pass
