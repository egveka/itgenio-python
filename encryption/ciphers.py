alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for symbol in plaintext.lower():
        if symbol == " ":
            ciphertext += symbol
            continue      
        index = alphabet.find(symbol)
        new_index = (index + key)%26
        new_letter = alphabet[new_index]
        ciphertext += new_letter
    return ciphertext

# print(caesar_encrypt("cat tail", 26))

def caesar_decrypt(text, key):
    deciphertext = ""
    for symbol in text.lower():
        if symbol == " ":
            deciphertext += " "
        else:
            index = alphabet.find(symbol)
            new_index = (index - key)%26
            new_letter = alphabet[new_index]
            deciphertext += new_letter
    return deciphertext

# print(caesar_decrypt("gex", 4))
# def hacking_caesar():
#     encrypted = "tlt xjxwfkd elt afa vlr al fq"
#     for i in range(26):
#         decrypted = caesar_decrypt(encrypted, i)
#         print(f"Key {i}:  {decrypted}")

# hacking_caesar()

#Atbash now
def atbash_encrypt(plaintext2):
    new_alphabet = alphabet[::-1]
    ciphertext2 = ""
    for char in plaintext2.lower():
        if char == " ":
            ciphertext2 += char
            continue
        index = alphabet.find(char)
        letter = new_alphabet[index]
        ciphertext2 += letter
    return ciphertext2
print(atbash_encrypt("itgenio"))