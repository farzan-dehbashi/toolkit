from abc import ABC, abstractclassmethod

class Stream(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def read(self):
        pass

    @abstractclassmethod
    def write(self):
        pass


