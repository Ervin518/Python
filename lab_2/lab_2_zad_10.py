while True:
    x_str = input("Podaj pierwszą liczbę całkowitą (0 kończy program): ")
    y_str = input("Podaj drugą liczbę całkowitą (0 kończy program): ")

    if not (x_str.lstrip('-').isdigit() and y_str.lstrip('-').isdigit()):
        print("Błąd: To nie są liczby całkowite! Spróbuj ponownie.")
        continue

    x = int(x_str)
    y = int(y_str)

    if x == 0 or y == 0:
        print("Podano 0. Koniec programu.")
        break

    print("Iloczyn:", x, "*", y, "=", x * y)