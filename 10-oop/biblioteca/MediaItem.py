from abc import ABC, abstractmethod

class MediaItem():
    def __init__(self, titolo: str, anno: str):
        self.titolo = titolo
        self.anno = anno
        self.disponibile = True
    
    @abstractmethod
    def prestito(self):
        pass
    
    @abstractmethod
    def restituzione(self):
        pass

    def descrivi(self):
        print(f'[{self.anno}] {self.titolo} Disponibile: {"Sì" if self.disponibile else "No"}')
    
    def __str__(self):
        return f'{self.__class__.__name__}: {self.titolo} ({self.anno})'