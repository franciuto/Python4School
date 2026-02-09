user = input("enter word: ")
dict1 = {}

for letter in user: 
    if not letter in dict1:
        dict1[letter] = 1
    else:
        dict1[letter] += 1

for letter in dict1:
    print(f'{letter} => {dict1[letter]}')
