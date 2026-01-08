from tkinter import*

window = Tk()
window.geometry("350x300")
window.title("Encrypting")
window.resizable(False, False)

lb1 = LabelFrame(text="Data")
lb2 = LabelFrame(text="Encrypted Text Messages")

key_label = Label(lb1, text="Enter key:")
keybox = Entry(lb1)
text_label = Label(lb1, text="Enter text:")
plaintextbox = Entry(lb1)

caesar_label = Label(lb2, text="Caesar's cipher", width=20)
c_l2 = Label(lb2, text="", width=20)
atbash_label = Label(lb2, text="Atbash cipher", width=20)
a_l2 = Label(lb2, text="", width=20)
encrypt_button = Button(lb2, width=10, text="Encrypt")

lb1.pack()
key_label.pack()
keybox.pack()
text_label.pack()
plaintextbox.pack()

lb2.pack()
caesar_label.pack()
c_l2.pack()
atbash_label.pack()
a_l2.pack()
encrypt_button.pack()

if __name__ == "__main__":
    window.mainloop()