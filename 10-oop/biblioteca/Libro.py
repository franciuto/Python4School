from MediaItem import MediaItem

class Libro(MediaItem):
    def __init__(self, titolo, anno, autore: str, pagine: int):
        super().__init__(titolo, anno)
        self.autore = autore
        self.pagine = pagine
    
    def prestito(self):
        if self.disponibile:
            self.disponibile = False
            return "Prestito avvenuto"
        else:
            return "Libro già in prestito"
    
    def restituzione(self):
        if not self.disponibile:
            self.disponibile = True
            return "Restituzione avvenuta"
        else:
            return "Libro non in prestito"
    
    def __str__(self):
        return f'{super().__str__()} autore={self.autore} pagine={self.pagine}'