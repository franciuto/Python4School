class Lettore:
    def __init__(self):
        self.permesso_lettura = True

    def mostra_permessi(self):
        return "leggere"


class Scrittore:
    def __init__(self):
        self.permesso_scrittura = True

    def mostra_permessi(self):
        return "scrivere"


class Amministratore(Lettore, Scrittore):
    def __init__(self):
        Lettore.__init__(self)
        Scrittore.__init__(self)

    def mostra_permessi(self):
        p1 = Lettore.mostra_permessi(self)
        p2 = Scrittore.mostra_permessi(self)
        return f"{p1} e {p2}"


# Creazione oggetti
l = Lettore()
s = Scrittore()
a = Amministratore()

print("Lettore:", l.mostra_permessi())
print("Scrittore:", s.mostra_permessi())
print("Amministratore:", a.mostra_permessi())

for cls in Amministratore.mro():
    print(cls)