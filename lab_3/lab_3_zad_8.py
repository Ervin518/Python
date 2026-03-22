import functools

wynik = functools.reduce(lambda x, y: x * y, range(1, 100))
print("Wynik mnożenia zakresu 1-99 to:\n", wynik)