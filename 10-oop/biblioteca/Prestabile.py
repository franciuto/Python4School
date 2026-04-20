from abc import ABC, abstractmethod

class Prestabile(ABC):
    @abstractmethod
    def prestito(self):
        pass

    @abstractmethod
    def restituzione(self):
        pass