import random
from sys import getsizeof
from datetime import datetime
from itertools import chain

n = 1000000
lista1 = [random.randint(1, 100) for _ in range(n)]
lista2 = [random.randint(1, 100) for _ in range(n)]
lista3 = [random.randint(1, 100) for _ in range(n)]

czas_start = datetime.now()
parzyste_a = []
nieparzyste_a = []
for element in lista1 + lista2 + lista3:
    if element % 2 == 0:
        parzyste_a.append(element)
    else:
        nieparzyste_a.append(element)
czas_a = datetime.now() - czas_start
pamiec_a = getsizeof(parzyste_a) + getsizeof(nieparzyste_a)

czas_start = datetime.now()
wszystkie_b = lista1 + lista2 + lista3
parzyste_b = [x for x in wszystkie_b if x % 2 == 0]
nieparzyste_b = [x for x in wszystkie_b if x % 2 != 0]
czas_b = datetime.now() - czas_start
pamiec_b = getsizeof(parzyste_b) + getsizeof(nieparzyste_b)

czas_start = datetime.now()
parzyste_c = list(filter(lambda x: x % 2 == 0, chain(lista1, lista2, lista3)))
nieparzyste_c = list(filter(lambda x: x % 2 != 0, chain(lista1, lista2, lista3)))
czas_c = datetime.now() - czas_start
pamiec_c = getsizeof(parzyste_c) + getsizeof(nieparzyste_c)

czas_start = datetime.now()
parzyste_d = (x for x in chain(lista1, lista2, lista3) if x % 2 == 0)
nieparzyste_d = (x for x in chain(lista1, lista2, lista3) if x % 2 != 0)
czas_d = datetime.now() - czas_start
pamiec_d = getsizeof(parzyste_d) + getsizeof(nieparzyste_d)

print("A) Imperatywnie:     Czas =", czas_a.microseconds, " Pamiec =", pamiec_a)
print("B) Funkcyjnie:       Czas =", czas_b.microseconds, " Pamiec =", pamiec_b)
print("C) Wyzszego rzedu:   Czas =", czas_c.microseconds, " Pamiec =", pamiec_c)
print("D) Generator:        Czas =", czas_d.microseconds, " Pamiec =", pamiec_d)