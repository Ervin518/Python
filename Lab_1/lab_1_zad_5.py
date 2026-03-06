liczba1 = int(input("Podaj pierwsza liczbe: "))
liczba2 = int(input("Podaj druga liczbe: "))

suma = liczba1 + liczba2

if suma % 2 == 0:
    print("Suma wynosi", suma, "i jest PARZYSTA.")
else:
    print("Suma wynosi", suma, "i jest NIEPARZYSTA.")