from abc import ABC, abstractmethod

class InternalStorageInterface(ABC):
    @abstractmethod
    def pull_from_dict(self, dictionary: dict):
        pass

    @abstractmethod
    def push_values_to_dict(self) -> dict:
        pass

    @abstractmethod
    def push_units_to_dict(self) -> dict:
        pass
