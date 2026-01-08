string = "b22%2mZUk$hv3'b'3s85Q#"
new_string = ""

for character in string:
    if character.isalpha():
        new_string += "1"
    elif character.isdigit():
        new_string += "2"
    else:
        new_string += "3"
print(new_string)