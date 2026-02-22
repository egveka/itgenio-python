import pickle

with open("lesson-42/cities-europe.bin", "rb") as file:
    cities = pickle.load(file)
print(len(cities))

cities1 = []
for city in cities:
    counter = 0
    for c in city:
        if c.isupper():
            counter += 1
    if counter == 1:
        cities1.append(city)
print(len(cities1))

cities2 = []
for city in cities1:
    if city[0].lower() == city[-1].lower():
        cities2.append(city)
print(len(cities2))

cities3 = []
vowels = "aeioyu"
for city in cities2:
    if city[1].lower() == city[-2].lower() and city[1].lower() in vowels:
        cities3.append(city)
print(len(cities3))

cities4 = []
for city in cities3:
    counter_w = 0
    for ch in city:
        if ch.lower() == "w":
            counter_w +=1
    if counter_w >= 1:
        cities4.append(city)
print(len(cities4))

res = []
res.append(min(cities4, key=len))
with open("lesson-42/letter.pickle", "wb") as file:
    pickle.dump(res, file)