from menu import Catalogo
from coffee_maker import Macchinetta
from money_machine import Cassa

catalogo = Catalogo()
macchinetta = Macchinetta()
cassa = Cassa()

attivo = True

while attivo:
    scelta = input(f"Cosa vuoi ordinare? ({catalogo.lista_nomi()}): ")

    if scelta == "spegni":
        attivo = False
    elif scelta == "stato":
        macchinetta.stato()
        cassa.stato()
    else:
        bevanda = catalogo.cerca(scelta)
        if bevanda:
            if macchinetta.scorte_sufficienti(bevanda):
                if cassa.paga(bevanda.prezzo):
                    macchinetta.prepara(bevanda)
