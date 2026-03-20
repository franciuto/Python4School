# Lista di personaggi famosi
dati_personaggi = [
    {"nome": "Albert Einstein",     "professione": "scienziato", "nazionalita": "tedesca",    "epoca": "XX secolo",   "genere": "maschio"},
    {"nome": "Leonardo da Vinci",   "professione": "artista",    "nazionalita": "italiana",   "epoca": "XV secolo",   "genere": "maschio"},
    {"nome": "Marie Curie",         "professione": "scienziato", "nazionalita": "polacca",    "epoca": "XX secolo",   "genere": "femmina"},
    {"nome": "Napoleone Bonaparte", "professione": "politico",   "nazionalita": "francese",   "epoca": "XIX secolo",  "genere": "maschio"},
    {"nome": "Frida Kahlo",         "professione": "artista",    "nazionalita": "messicana",  "epoca": "XX secolo",   "genere": "femmina"},
    {"nome": "Isaac Newton",        "professione": "scienziato", "nazionalita": "britannica", "epoca": "XVII secolo", "genere": "maschio"},
    {"nome": "Cleopatra",           "professione": "politico",   "nazionalita": "egiziana",   "epoca": "I secolo",    "genere": "femmina"},
    {"nome": "Nikola Tesla",        "professione": "scienziato", "nazionalita": "serba",      "epoca": "XIX secolo",  "genere": "maschio"},
    {"nome": "Coco Chanel",         "professione": "artista",    "nazionalita": "francese",   "epoca": "XX secolo",   "genere": "femmina"},
    {"nome": "Galileo Galilei",     "professione": "scienziato", "nazionalita": "italiana",   "epoca": "XVI secolo",  "genere": "maschio"},
]

# Lista di domande disponibili
# "attributo" corrisponde a una chiave del dizionario personaggio
# "valore_atteso" è il valore su cui la domanda interroga
dati_domande = [
    {"testo": "È uno scienziato?",       "attributo": "professione", "valore_atteso": "scienziato"},
    {"testo": "È un artista?",           "attributo": "professione", "valore_atteso": "artista"},
    {"testo": "È un politico?",          "attributo": "professione", "valore_atteso": "politico"},
    {"testo": "È italiano?",             "attributo": "nazionalita", "valore_atteso": "italiana"},
    {"testo": "È francese?",             "attributo": "nazionalita", "valore_atteso": "francese"},
    {"testo": "È tedesco?",              "attributo": "nazionalita", "valore_atteso": "tedesca"},
    {"testo": "È britannico?",           "attributo": "nazionalita", "valore_atteso": "britannica"},
    {"testo": "È vissuto nel XX secolo?",   "attributo": "epoca", "valore_atteso": "XX secolo"},
    {"testo": "È vissuto nel XIX secolo?",  "attributo": "epoca", "valore_atteso": "XIX secolo"},
    {"testo": "È vissuto nel XVII secolo?", "attributo": "epoca", "valore_atteso": "XVII secolo"},
    {"testo": "È di genere femminile?",  "attributo": "genere",      "valore_atteso": "femmina"},
]
