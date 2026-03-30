from itertools import cycle
a = int(input("Podaj liczbe: "))
i = 0

for n in cycle('INFORMATYKA'):
    if i >= a:
        break
    else:
        print(n)
        i += 1