import tkinter as tk
from tkinter.messagebox import showinfo


def pokaz_wynik():
    wybrane = []
    if var_agd.get() == 1: wybrane.append("AGD")
    if var_kosmetyki.get() == 1: wybrane.append("Kosmetyki")
    if var_odziez.get() == 1: wybrane.append("Odzież")

    if not wybrane:
        showinfo("Wynik", "Nic nie wybrano!")
    else:
        wynik_tekst = "Kupujesz: " + ", ".join(wybrane)
        showinfo("Wynik", wynik_tekst)


root = tk.Tk()
root.title("Ankieta Świąteczna")

tk.Label(root, text="Co najczęściej kupujesz dla rodziny w prezencie?").pack(pady=10)

var_agd = tk.IntVar()
var_kosmetyki = tk.IntVar()
var_odziez = tk.IntVar()

tk.Checkbutton(root, text="AGD", variable=var_agd).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Kosmetyki", variable=var_kosmetyki).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Odzież", variable=var_odziez).pack(anchor="w", padx=20)

tk.Button(root, text="Sprawdź", command=pokaz_wynik).pack(pady=15)

root.mainloop()