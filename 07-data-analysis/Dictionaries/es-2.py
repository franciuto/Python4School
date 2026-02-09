student = {
    "name" : "luca",
    "age" : 17,
    "class" : "3A",
    "average" : 7.5,
    "passed" : True
}

student["average"] = 8
print(f'Student datas:\nname: {student["name"]}\nage: {student["age"]}\naverage: {student["average"]}')

print(f'la chiave "address" esiste nel dizionario? {"address" in student}')