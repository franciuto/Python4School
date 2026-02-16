import nazioni
import random

score = 0

while True:
    country = random.choice(nazioni.countries)
    question_type = random.choice(["capital", "continent"])

    if question_type == "capital":
        print(f'\nQual è la capitale di {country["name"]}?')
        correct = country["capital"]
        wrong = []
        while len(wrong) < 3:
            option = random.choice(nazioni.countries)["capital"]
            if option != correct and option not in wrong:
                wrong.append(option)
    else:
        print(f'\nIn quale continente si trova {country["name"]}?')
        correct = country["continent"]
        wrong = []
        continents = list(set(c["continent"] for c in nazioni.countries if c["continent"] != correct))
        wrong = random.sample(continents, 3)

    options = wrong + [correct]
    random.shuffle(options)

    for i in range(len(options)):
        print(f'{i + 1}. {options[i]}')

    answer = input("Risposta: ")

    if options[int(answer) - 1] == correct:
        print("Corretto!")
        score += 1
    else:
        print(f'Sbagliato La risposta corretta era: {correct}')
        print(f'Punteggio finale: {score}')
        break
