rubrica = {}

def user_prompt():
    print(f'Select action:\n1. Add a contact\n2. Find a number\n3. View contacts\n4. Exit')
    return int(input("Choose action: "))

def add_number(rubrica):
    rubrica[input("Insert contact name: ")] = input("Insert phone number: ")

def find_number(rubrica, query):
    return rubrica.get(query)

def view_contacts(rubrica):
    if not rubrica:
        print("No contacts yet!")
        return
    for name, number in rubrica.items():
        print(f"  {name}: {number}")

while True:
    action = user_prompt()
    match action:
        case 4:
            break
        case 1:
            add_number(rubrica)
        case 2:
            result = find_number(rubrica, input("Inserisci nome da cercare: "))
            if result:
                print(f"Risultato: {result}")
            else:
                print("Contact not found!")
        case 3:
            print("Contacts:")
            view_contacts(rubrica)
        case _:
            print("Invalid action!")
