from MediaItem import MediaItem
from Prestabile import Prestabile

class EBook(MediaItem, Prestabile):
    def __init__(self, titolo: str, anno: str, formato: str, dimensione_mb: float):
        super().__init__(titolo, anno)
        self.formato = formato
        self.dimensione_mb = dimensione_mb
        self.num_prestiti = 0

    def prestito(self):
        if self.disponibile:
            self.disponibile = False
            self.num_prestiti += 1
            return "Prestito avvenuto"
        else:
            return "EBook già in prestito"

    def restituzione(self):
        if not self.disponibile:
            self.disponibile = True
            return "Restituzione avvenuta"
        else:
            return "EBook non in prestito"

    def statistiche(self):
        print(f"EBook '{self.titolo}' prestato {self.num_prestiti} volte")

    def __str__(self):
        return f'{super().__str__()} formato={self.formato} dimensione_mb={self.dimensione_mb}'