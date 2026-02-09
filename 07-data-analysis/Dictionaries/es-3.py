grades = {
"math": 8,
"italian": 7,
"history": 6,
"english": 9
}

print(f'Materie: {", ".join(grades.keys())}')
print(f'Voti: {", ".join(map(str, grades.values()))}\n\n')

sum = 0
for subject in grades:
    print(f'{subject} => {grades[subject]}')
    sum += grades[subject]

print(f'\nMedia: {sum / len(grades)}')