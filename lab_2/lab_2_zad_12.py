import random

losowe_liczby = random.sample(range(1000), 100)

parzyste = []
for liczba in losowe_liczby:
    if liczba % 2 == 0:
        parzyste.append(liczba)

parzyste.sort()

print("Posortowane liczby parzyste:")
print(parzyste)
