from Catalogo import Catalogo
from Libro import Libro
from Rivista import Rivista
from DVD import DVD
from Ebook import EBook


def main():
    catalogo = Catalogo()

    libro = Libro("Il nome della rosa", "1980", "Eco", 512)
    rivista = Rivista("Focus", "2024", 12, 6)
    dvd = DVD("Inception", "2010", "Nolan", 148)
    ebook = EBook("Clean Code", "2008", "EPUB", 3.4)

    catalogo.aggiungi(libro)
    catalogo.aggiungi(rivista)
    catalogo.aggiungi(dvd)
    catalogo.aggiungi(ebook)

    print("Catalogo iniziale:")
    for item in catalogo.disponibili():
        print(item)

    print("\nPrestito libro e DVD:")
    print(libro.prestito())
    print(dvd.prestito())

    print("\nPrestito EBook:")
    print(ebook.prestito())

    print("\nDisponibili dopo prestito:")
    for item in catalogo.disponibili():
        print(item)

    print("\nRestituzione libro:")
    print(libro.restituzione())

    print("\nFinale:")
    catalogo.stampa_catalogo()
    ebook.statistiche()


if __name__ == "__main__":
    main()
