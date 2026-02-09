books = [
    {"title": "1984", "author": "Orwell", "year": 1949},
    {"title": "Dune", "author": "Herbert", "year": 1965},
    {"title": "Foundation", "author": "Asimov", "year": 1951}
]

print("Libri:")
for book in books:
    print(f'- {book["title"]}')

query = input("inserisci libro da cercare: ")
for book in books:
    if query.lower() in book["title"].lower():
        print(f'{book["title"]} => {book["author"]}')