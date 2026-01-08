dictionary = {"Hello":"Hola", "Goodbye":"Adios", "Thanks":"Gracias",
            "Please":"Por favor", "Water":"Agua", "House":"Casa",
            "Dog":"Perro", "Cat":"Gato", "Friend":"Amigo", "School":"Eschuela"}
word = input()
for key,value in dictionary.items():
    if word in dictionary:
        print(value)
        break
else:
    print("Word not found")