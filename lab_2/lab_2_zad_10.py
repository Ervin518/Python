while True:
    x_str = input("Podaj pierwsza liczbe (0 konczy program): ")
    y_str = input("Podaj druga liczbe (0 konczy program): ")

    if not (x_str.isdigit() and y_str.isdigit()):
        print("Blad: podaj liczby calkowite dodatnie!")
        continue

    x = int(x_str)
    y = int(y_str)

    if x == 0 or y == 0:
        print("Podano 0. Koniec programu.")
        break

    print("Iloczyn:", x * y)
