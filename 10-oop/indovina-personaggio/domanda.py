from personaggio import Personaggio
class Domanda():
    def __init__(self, testo, attributo, valore_atteso):
        self.testo = testo
        self.attributo = attributo
        self.valore_atteso = valore_atteso
    
    def controlla(self, Personaggio):
        valore = getattr(Personaggio, self.attributo)
        return valore == self.valore_atteso