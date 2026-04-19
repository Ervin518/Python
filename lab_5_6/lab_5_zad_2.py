import pickle

def konkretne_liczby(x, y):

    numbers = list(range(x, y+1))

    wynikowe_liczby = [z for z in numbers if z % 7 == 0 and z % 5 != 0]

    tekst_wynik = ", ".join(map(str, wynikowe_liczby))
    print(tekst_wynik)

    plik_pkl = "dane.pkl"
    with open(plik_pkl, 'wb') as file:
        pickle.dump(wynikowe_liczby, file)

try:
    poczatek = int(input("Podaj poczatek przedzialu: "))
    koniec = int(input("Podaj koniec przedzialu: "))

    konkretne_liczby(poczatek, koniec)

except ValueError:
    print("Blad: Musisz podac liczby calkowite!")