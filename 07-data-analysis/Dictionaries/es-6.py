import os
rubrica = {}

def user_prompt():
    print(f'Select action:\n1. Add a contact\n2. Find a number\n3. View contacts\n4. Exit')
    return int(input("Choose action: "))

def add_number(rubrica):
    rubrica[input("Insert contact name: ")] = input("Insert phone number: ")
    
def find_number(rubrica, query):
    return rubrica.get(query)

while True:
    os.system("cls" if os.name == "nt" else "clear")
    action = user_prompt()
    match action:
        case 4:
            break
        case 1:
            add_number(rubrica)
        case 2:
            query = input("Inserisci ricerca: ")
            print(f'Risultato: {rubrica.get(query) if rubrica.get(query) else "Non trovato"}')
        case 3:
            for name, number in rubrica.items():
                print(f'- {name}: {number}')