import interface
import generator

def generate():
    interface.password_e.delete(0, "end")
    lowercase_check = interface.lowercase.get()
    numbers_check = interface.number.get()
    special_check = interface.special.get()
    uppercase_check = interface.uppercase.get()
    result = generator.generate_password(lowercase_check, numbers_check, special_check, uppercase_check)
    interface.password_e.insert(0, result)

interface.button.config(command=generate)
interface.window.mainloop()