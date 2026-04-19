from functools import reduce

n = int(input("Podaj ktory element ciagu Fibonacciego wypisac: "))

if n <= 0:
    print("Podaj liczbe wieksza od zera.")
elif n == 1:
    print("N-ty element ciagu Fibonacciego to: 0")
elif n == 2:
    print("N-ty element ciagu Fibonacciego to: 1")
else:
    ciag = reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
    
    print("Wygenerowany ciag:", ciag)
    print("N-ty element ciagu Fibonacciego to:", ciag[-1])
