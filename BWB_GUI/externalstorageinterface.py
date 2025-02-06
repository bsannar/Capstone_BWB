from abc import ABC, abstractmethod

class ExternalStorageInterface:
    @abstractmethod
    def pull_from_storage():
        pass

    @abstractmethod
    def push_to_storage(data: dict):
        pass
