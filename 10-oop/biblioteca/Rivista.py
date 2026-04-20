from MediaItem import MediaItem

class Rivista(MediaItem):
    def __init__(self, titolo, anno, numero: int, mese: int):
        super().__init__(titolo, anno)
        self.numero = numero
        self.mese = mese
    
    def prestito(self):
        if self.disponibile:
            self.disponibile = False
            return f'Prestito di N.{self.numero} del mese {self.mese} avvenuto'
        else:
            return "Rivista già in prestito"
        
    def restituzione(self):
        if not self.disponibile:
            self.disponibile = True
            return "Restituzione avvenuta"
        else:
            return "Rivista non in prestito"

    def __str__(self):
        return f'{super().__str__()} numero={self.numero} mese={self.mese}'
