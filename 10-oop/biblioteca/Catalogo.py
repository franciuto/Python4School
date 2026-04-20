from MediaItem import MediaItem
from Libro import Libro
from Rivista import Rivista
from DVD import DVD
from Ebook import EBook

class Catalogo():
    def __init__(self):
        self.articoli = []
    
    def aggiungi(self, item: MediaItem) -> bool:
        if isinstance(item, MediaItem):
            self.articoli.append(item)
            return True
        else: return False
    
    def stampa_catalogo(self):
        print("Articoli:")
        for i, item in enumerate(self.articoli):
            print(f"[{i}] {item}")
            
    def disponibili(self) -> list:
        r = []
        for articolo in self.articoli:
            if articolo.disponibile:
                r.append(articolo)
        return r

    def cerca_per_tipo(self, tipo: type) -> list:
        r = []
        for articolo in self.articoli:
            if isinstance(articolo, tipo):
                r.append(articolo)
        return r

    def report(self) -> None:
        libri = "\n".join(map(str, self.cerca_per_tipo(Libro))) or "(nessuno)"
        riviste = "\n".join(map(str, self.cerca_per_tipo(Rivista))) or "(nessuna)"
        dvd = "\n".join(map(str, self.cerca_per_tipo(DVD))) or "(nessuno)"
        ebook = "\n".join(map(str, self.cerca_per_tipo(EBook))) or "(nessuno)"

        print(
            f"Articoli disponibili: {len(self.articoli)} => Disponibili: {len(self.disponibili())} | "
            f"In prestito: {len(self.articoli) - len(self.disponibili())}\n--------------------\n"
            f"Libri:\n{libri}\n\n"
            f"Riviste:\n{riviste}\n\n"
            f"DVD:\n{dvd}\n\n"
            f"EBook:\n{ebook}"
        )