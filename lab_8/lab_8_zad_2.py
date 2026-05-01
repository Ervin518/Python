import tkinter as tk
from tkinter.messagebox import showerror


def oblicz():
    try:
        k = float(entry_k.get())
        n = int(entry_n.get())

        if not 1000 <= k <= 10000 or n <= 0:
            return showerror("Błąd", "Kwota: 1000-10000 zł. Miesiące > 0.")

        q = 1.1225
        rata = (k * q ** n * (1 - q)) / (1 - q ** n)

        kolor = "green" if rata <= 500 else "orange" if rata <= 1500 else "red"

        tekst_wyniku = "Rata: " + str(round(rata, 2)) + " zł"
        wynik_lbl.config(text=tekst_wyniku, fg=kolor)

    except ValueError:
        showerror("Błąd", "Wprowadź poprawne liczby!")


root = tk.Tk()
root.title("Kredyt")

tk.Label(root, text="Kwota (1000-10000 zł):").grid(row=0, column=0)
entry_k = tk.Entry(root)
entry_k.grid(row=0, column=1)

tk.Label(root, text="Miesiące:").grid(row=1, column=0)
entry_n = tk.Entry(root)
entry_n.grid(row=1, column=1)

tk.Button(root, text="Oblicz", command=oblicz).grid(row=2, columnspan=2)
wynik_lbl = tk.Label(root, text="Rata: 0.00 zł", font=("Arial", 12, "bold"))
wynik_lbl.grid(row=3, columnspan=2)

root.mainloop()