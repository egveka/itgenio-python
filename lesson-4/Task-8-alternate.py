correct = False

while not correct:
    print("Password:")
    pwd = input()
    print("Again:")
    confirm = input()
    if pwd != confirm:
        print("Different")
    elif "123" in pwd:
        print("Simple!")
    else:
        print("OK")
        correct = True