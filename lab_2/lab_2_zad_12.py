import random

losowe_liczby = []
for _ in range(100):
    losowe_liczby.append(random.randint(1, 1000))

parzyste = []
for liczba in losowe_liczby:
    if liczba % 2 == 0:
        parzyste.append(liczba)

parzyste.sort()

print("Posortowane liczby parzyste:")
print(parzyste)