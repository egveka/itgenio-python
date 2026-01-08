import interface
import zodiac

def define_zodiac():
    day = int(interface.e_d.get())
    month = int(interface.e_m.get())
    index = zodiac.define(day, month)
    name = interface.zodiac_names[index]
    file = interface.zodiac_files[index]
    interface.gif.config(file=f"Zodiacs/img/{file}")
    interface.name.config(text=name)

interface.button.config(command=define_zodiac)

interface.window.mainloop()