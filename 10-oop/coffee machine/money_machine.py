
class Cassa:
    def __init__(self):
        self.incasso = 0.0

    def stato(self):
        print(f"Incasso totale: {self.incasso:.2f} euro")

    def inserisci_soldi(self):
        print("Inserisci le monete.")
        totale = 0.0
        totale += int(input("Monete da 1 euro: ")) * 1.00
        totale += int(input("Monete da 50 cent: ")) * 0.50
        totale += int(input("Monete da 20 cent: ")) * 0.20
        totale += int(input("Monete da 10 cent: ")) * 0.10
        return totale

    def paga(self, prezzo):
        inserito = self.inserisci_soldi()
        if inserito >= prezzo:
            resto = round(inserito - prezzo, 2)
            if resto > 0:
                print(f"Resto: {resto:.2f} euro")
            self.incasso += prezzo
            return True
        print("Importo insufficiente. Denaro restituito.")
        return False
