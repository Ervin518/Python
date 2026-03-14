wynik = []

for i in range(1, 1001):
    czy_wszystkie_parzyste = True
    for cyfra in str(i):
        if int(cyfra) % 2 != 0:
            czy_wszystkie_parzyste = False
            break

    if czy_wszystkie_parzyste:
        wynik.append(str(i))

print(", ".join(wynik))