import pickle

data = ["Russia", "Canada", "China", "United States", "Brazil", "Australia", "India", "Argentina", "Kazakhstan"]
# byteststream = pickle.dumps(data)
# print(byteststream)
# normal_data = pickle.loads(byteststream)
# print(normal_data)

# with open ("lesson-41/countries.bin", "wb")as file:
#     pickle.dump(data, file)

# with open("lesson-41/countries.bin", "rb") as file:
#         text = file.read()
# print(text)

# with open("lesson-41/countries.bin", "rb") as file:
#         data = pickle.load(file)
# print(data)

# with open("lesson-41/lists.bin", "wb")as file:
#         pickle.dump([1,2,3], file)
#         pickle.dump([4,5,6], file)
#         pickle.dump([7,8,9], file)

with open("lesson-41/lists.bin", "rb") as file:
        print(pickle.load(file))
        print(pickle.load(file))
        print(pickle.load(file))

# with open("lesson-41/lists.bin", "rb") as file:
#         print(pickle.load(file))
#         print(pickle.load(file))
#         print(pickle.load(file))
#         print(pickle.load(file))