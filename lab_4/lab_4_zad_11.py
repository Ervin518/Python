import random
from itertools import groupby

jezyki = ['python', 'java', 'C++', 'C#', 'javascript', 'php']

list_prog = []
for _ in range(10000):
    list_prog.append(random.choice(jezyki))

szukany_jezyk = 'python'
print("Szukamy ilosci wystapien jezyka:", szukany_jezyk)
print("-" * 40)

licznik_a = 0
for j in list_prog:
    if j == szukany_jezyk:
        licznik_a = licznik_a + 1

print("a) Wynik imperatywnie (petla for):", licznik_a)

wynik_b = list(filter(lambda x: x == szukany_jezyk, list_prog))
licznik_b = len(wynik_b)

print("b) Wynik funkcyjnie (filter + len):", licznik_b)

zmapowane = map(lambda x: (x, 1), list_prog)

posortowane = sorted(zmapowane, key=lambda x: x[0])

zredukowane = []
for nazwa_jezyka, podgrupa in groupby(posortowane, key=lambda x: x[0]):
    suma_wystapien = sum(element[1] for element in podgrupa)
    zredukowane.append((nazwa_jezyka, suma_wystapien))

licznik_c = 0
for wynik in zredukowane:
    if wynik[0] == szukany_jezyk:
        licznik_c = wynik[1]

print("c) Wynik MapReduce (groupby + sum):", licznik_c)
print("-" * 40)
print("Wszystkie wyniki po redukcji:", zredukowane)