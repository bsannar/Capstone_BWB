from abc import ABC, abstractmethod

class ExternalStorageInterface:
    @abstractmethod
    def pull_data_from_storage():
        pass

    @abstractmethod
    def push_data_to_storage():
        pass
