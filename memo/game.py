from tkinter import *
from dictionary import words
from random import choice
from random import shuffle

root = Tk()
root.geometry("500x230")
root.resizable(True, True)
root.title("Memo")

menu1 = Button(text="Can you translate\nENG -> RUS", width=300, height=7, command=lambda lang = "eng": startLevel(lang))
menu2 = Button(text="Can you translate\nRUS -> ENG", width=300, height=7, command=lambda lang = "rus": startLevel(lang))

def showMenu():
    menu1.pack()
    menu2.pack()
    menu1.focus_force()
    menu2.focus_force()

def hideMenu():
    menu1.forget()
    menu2.forget()

showMenu()
cnt = 0

rus_words = words
eng_words = dict([[v, k] for k, v in words.items()])

print(rus_words)
print(eng_words)

def chooseWord(language):
    if language == "rus":
        word = choice(list(rus_words.keys()))
        random_Letters = [choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")for i in range(25-len(word))]
        translated_word = rus_words[word]
    else:
        word = choice(list(eng_words.keys()))
        random_Letters = [choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")for i in range(25-len(word))]
        translated_word = eng_words[word]
    return word, translated_word

def startLevel(lang):
    global cnt
    hideMenu()
    word, translated_word = chooseWord(lang)
    if lang == "rus":
        random_Letters = [choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")for i in range(25-len(word))]
        label_1 = Label(root, text=word, font=("Arial", 20))
        letters = [i for i in(rus_words[word])]
        letters += random_Letters
    else:
        random_Letters = [choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")for i in range(25-len(word))]
        label_1 = Label(root, text=word, font=("Arial", 20))
        letters = [i for i in(eng_words[word])]
        letters += random_Letters
    shuffle(letters)
    buttons = []
    column = 0
    row = 3
    label_1.grid(row=0, column=0, columnspan=3)
    label2 = Label(root, text="",font=("Arial", 20))
    label2.grid(row=0, column=3, columnspan=3)
    for i in range(0, len(letters)):
        buttons.append(Button(root, text=letters[i],  width=5))
        buttons[i].config(command=lambda button=buttons[i]: chooseLetter(button))
        buttons[i].grid(column=column, row=row, sticky="ew")
        column += 1
        if column > 4:
            column = 0
            row += 1
    def chooseLetter(button):
        global cnt
        print(button.cget("text"), translated_word[cnt])
        if button.cget("text") == translated_word[cnt]:
            button.config(state=DISABLED)
            label2.config(text=label2.cget("text") + translated_word[cnt])
            cnt+=1
        elif button.cget("state") != DISABLED and button.cget("text") != translated_word[cnt]:
            for i in buttons:
                i.config(state=NORMAL)
            label2.config(text="")
            cnt = 0
        if cnt > len(translated_word)-1:
            delete()
            showMenu()
            cnt = 0
            menu1.focus()
            menu2.focus()

    def delete():
        del letters[:]
        for i in buttons:
            i.destroy()
        del buttons[:]
        label_1.destroy()
        label2.destroy()

root.mainloop()