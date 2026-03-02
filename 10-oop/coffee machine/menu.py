class Bevanda:
    def __init__(self, nome, acqua, latte, caffe, prezzo):
        self.nome = nome
        self.acqua = acqua
        self.latte = latte
        self.caffe = caffe
        self.prezzo = prezzo


class Catalogo:
    def __init__(self):
        self.bevande = [
            Bevanda("americano", 150, 0, 20, 1.0),
            Bevanda("cappuccino", 100, 100, 20, 2.0),
            Bevanda("macchiato", 50, 30, 15, 1.5),
        ]

    def lista_nomi(self):
        nomi = ""
        for b in self.bevande:
            nomi += b.nome + "/"
        return nomi

    def cerca(self, nome):
        for b in self.bevande:
            if b.nome == nome:
                return b
        print("Bevanda non trovata.")
        return None
