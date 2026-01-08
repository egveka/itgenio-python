import interface
from ciphers import caesar_encrypt
from ciphers import atbash_encrypt

def encrypt():
    plaintext = interface.plaintextbox.get()
    key = (int(interface.keybox.get()))
    interface.c_l2.config(text=caesar_encrypt(plaintext, key))
    interface.a_l2.config(text=atbash_encrypt(plaintext))
interface.encrypt_button.config(command=encrypt)

interface.window.mainloop()