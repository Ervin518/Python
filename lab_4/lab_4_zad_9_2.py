from functools import reduce

n = int(input("Podaj liczbe: "))

if n <= 0:
    print("Podaj liczbe wieksza od zera.")
else:
    wynik = reduce(lambda x, _: (x[1], x[0] + x[1]), range(n - 1), (0, 1))

    print("N-ty element ciagu Fibonacciego to:", wynik[0])