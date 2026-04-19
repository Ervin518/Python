def potegi(*args):
    if len(args) >= 100:
        print("Za duzo argumentow")
    elif len(args) == 0:
        print("Brak argumentow")
    else:
        wyniki = []
        for i in range(len(args)):
            nazwa = "x" + str(i+1)
            try:
                x = float(args[i])
                globals()[nazwa] = x
                potega = globals()[nazwa] ** globals()[nazwa]
                wyniki.append(potega)
            except ValueError:
                print("To nie jest liczba")
        return wyniki

argumenty = input("Podaj argumenty: ")
wynik_koncowy = argumenty.split(",")
print("Wyniki: ", potegi(*wynik_koncowy))
