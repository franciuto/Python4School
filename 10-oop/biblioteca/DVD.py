from MediaItem import MediaItem

class DVD(MediaItem):
    def __init__(self, titolo, anno, regista: str, durata: int):
        super().__init__(titolo, anno)
        self.regista = regista
        self.durata = durata

    def prestito(self):
        if self.disponibile:
            self.disponibile = False
            return f'Prestito avvenuto regista: {self.regista} durata: {self.durata}'
        else:
            return "DVD già in prestito"

    def restituzione(self):
        if not self.disponibile:
            self.disponibile = True
            return "Restituzione avvenuta"
        else:
            return "DVD non in prestito"
        
    def __str__(self):
        return f'{super().__str__()} regista={self.regista} durata={self.durata}'