n = int(input("Podaj liczbe: "))

def gener(n):
    wartosc = 4
    for i in range(n):
        yield wartosc
        if i == 0:
            wartosc = 16
        else:
            wartosc = wartosc * 2

generator = gener(n)
for liczba in generator:
    print(liczba)