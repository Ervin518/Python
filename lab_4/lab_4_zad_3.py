from itertools import count

n = float(input("Podaj liczbe, wieksza niz 99: "))

if n <= 99:
    print("Podaj inna liczba")
else:
    for i in count(99, 5):
        if i < n:
            print(i)
        else:
            break