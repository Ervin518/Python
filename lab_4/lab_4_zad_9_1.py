import random

def gener_parzyste(n):
    wygenerowane = 0
    while wygenerowane < n:
        liczba = random.randint(0, 100000000)

        if liczba % 2 == 0:
            yield liczba
            wygenerowane += 1

generator = gener_parzyste(1000)
for liczba in generator:
    print(liczba)
