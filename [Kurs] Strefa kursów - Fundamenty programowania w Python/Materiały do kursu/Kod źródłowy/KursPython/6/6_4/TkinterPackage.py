from tkinter import *


def wyswietl():
    print("Nasz pierwszy program z graficznym interfejsem użytkownika!")


window = Tk()
window.geometry('400x100')
frame = Frame()
frame.pack(expand=True)
Label(
    master=frame,
    text="Witaj w aplikacji!",
    font=18
).pack(side=TOP)
Button(
    master=frame,
    text="Naciśnij, aby wyświetlić w konsoli...",
    command=wyswietl,
    font=18
).pack(side=BOTTOM)
window.mainloop()
