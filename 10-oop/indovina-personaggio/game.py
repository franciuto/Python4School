import random
from domanda import Domanda
from personaggio import Personaggio
class Game():
    def __init__(self, lista_personaggi, lista_domande):
        self.lista_personaggi = lista_personaggi
        self.lista_domande = lista_domande
        self.domande = []
        self.personaggi = []
        self.personaggio_segreto = None
        self.numero_domanda = 0
        self.domande_attributo = {"professione" : [], "nazionalita" : [], "epoca" : []}
        
    def instanzia_domande(self):
        for d_data in self.lista_domande:
            domanda_obj = Domanda(d_data["testo"], d_data["attributo"], d_data["valore_atteso"])
            self.domande.append(domanda_obj)
            
            if domanda_obj.attributo in self.domande_attributo:
                self.domande_attributo[domanda_obj.attributo].append(domanda_obj)


    def instanzia_personaggi(self):
        for p in self.lista_personaggi:
            self.personaggi.append(Personaggio(p["nome"], p["professione"], p["nazionalita"], p["epoca"], p["genere"]))
    
    def scegli_personaggio(self):
        self.personaggio_segreto = random.choice(self.personaggi)
    
    def next_question(self):
        current_questions_menu = []
        attribute_types = ["professione", "nazionalita", "epoca", "genere"]

        for attr_type in attribute_types:
            if self.domande_attributo.get(attr_type): 
                random_question = random.choice(self.domande_attributo[attr_type])
                current_questions_menu.append(random_question)

        while True:
            print("\nScegli una domanda (0 per indovinare):")
            for i, question_obj in enumerate(current_questions_menu):
                print(f" {i+1}. {question_obj.testo}")
            
            choice = int(input("> "))
            if choice == 0:
                return "GUESS"
            elif 1 <= choice <= len(current_questions_menu):
                self.numero_domanda += 1
                return current_questions_menu[choice - 1]
            else:
                print("Scelta non valida")
        
    
    def guess_personaggio(self):
        print("\nChi pensi che sia?")
        guess = input("> ")
        if guess.lower() == self.personaggio_segreto.nome.lower():
            print("Corretto")
            return True
        else:
            print(f"Sbagliato")
            return False

    def play(self):
        self.instanzia_domande()
        self.instanzia_personaggi()
        self.scegli_personaggio()

        print("il personaggio segreto è stato estratto")

        game_over = False
        while not game_over:
            chosen_action = self.next_question()

            if chosen_action == "GUESS":
                if self.guess_personaggio():
                    game_over = True
                else:
                    print("sbagliato")
            elif chosen_action is None:
                print("nessuna domanda disponibile")
                game_over = True
            else:
                question_obj = chosen_action
                
                if question_obj.controlla(self.personaggio_segreto):
                    print("Risposta: Sì")
                else:
                    print("Risposta: No")
        
        print("\nBye")
        