class Macchinetta:
    def __init__(self):
        self.scorte = {
            "acqua": 500,
            "latte": 300,
            "caffe": 150,
        }

    def stato(self):
        print(f"Acqua: {self.scorte['acqua']}ml")
        print(f"Latte: {self.scorte['latte']}ml")
        print(f"Caffe: {self.scorte['caffe']}g")

    def scorte_sufficienti(self, bevanda):
        if bevanda.acqua > self.scorte["acqua"]:
            print("Acqua insufficiente.")
            return False
        if bevanda.latte > self.scorte["latte"]:
            print("Latte insufficiente.")
            return False
        if bevanda.caffe > self.scorte["caffe"]:
            print("Caffe insufficiente.")
            return False
        return True

    def prepara(self, bevanda):
        self.scorte["acqua"] -= bevanda.acqua
        self.scorte["latte"] -= bevanda.latte
        self.scorte["caffe"] -= bevanda.caffe
        print(f"Ecco il tuo {bevanda.nome}! Buona bevuta!")
