# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą
# Turėtų mygtuką su užrašu "Patvirtinti", kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"
# Būtų punktas "Išvalyti", kurį paspaudus išsitrintų tekstas eilutėje, kurioje spausdinamas pasisveikinimo tekstas
# Būtų punktas "Atkurti", kurį paspaudus pasisveikinimo teksto eilutėje butų atspausdintas paskutinis atspausdintas tekstas
# Būtų punktas "Išeiti", kurį paspaudus užsidarytų programos langas
# Tarp menių punktų "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys



from tkinter import Tk, Label, Entry, Button, Menu, StringVar, SUNKEN, W, E

langas = Tk()
issaugotas = StringVar()
def spausdinti():
    ivesta = laukas.get()
    rezultatas["text"] = f"Labas, {ivesta}!"
    laukas.delete(0, "end")
    issaugotas.set(rezultatas["text"])
    statusas["text"] = "Sukurta"

def spausdinti2(event):
    ivesta = laukas.get()
    rezultatas["text"] = f"Labas, {ivesta}!"
    laukas.delete(0, "end")
    issaugotas.set(rezultatas["text"])
    statusas["text"] = "Sukurta"
def trinti():
    rezultatas["text"] = ""
    statusas["text"] = "Išvalyta"

def prisiminti():
    rezultatas["text"] = issaugotas.get()
    statusas["text"] = "Atkurta"

def iseiti():
    langas.destroy()

langas.geometry("270x70")

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Ištrinti", command=trinti)
submeniu.add_command(label="Atkurti paskutinį", command=prisiminti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

vardas = Label(langas, text="Įveskite vardą")
laukas = Entry(langas)
mygtukas = Button(langas, text="Patvirtinti", command=spausdinti)
langas.bind("<Return>", spausdinti2)
langas.bind("<Escape>", lambda x: langas.destroy())
rezultatas = Label(langas, text="")
statusas = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)

vardas.grid(row=0, column=0)
laukas.grid(row=0, column=1)
laukas.focus()
mygtukas.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=3)
statusas.grid(row=2, columnspan=3, sticky=W+E)
langas.mainloop()
