def warunek(x):
    return x % 7 == 0 and x % 5 != 0

wynik_zad9 = list(filter(warunek, range(2000, 3201)))
print("Wynik zadania 9:\n", wynik_zad9)