def potegi(*args):
    if len(args) >= 100:
        print("Za duzo argumentow")
    elif len(args) == 0:
        print("Brak argumentow")
    else:
        wyniki = []
        for arg in args:
            x = float(arg)
            wyniki.append(x ** x)
        return wyniki

argumenty = input("Podaj argumenty: ")
wynik_koncowy = argumenty.split(",")
print("Wyniki: ", potegi(*wynik_koncowy))
