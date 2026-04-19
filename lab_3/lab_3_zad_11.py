def poziom(n):
    print("*" * n)

def pion(n):
    for i in range(n):
        print("*")

litera = input("Podaj litere (E lub L): ").upper()

if litera == 'E':
    poziom(5)
    pion(1)
    poziom(4)
    pion(1)
    poziom(5)
elif litera == 'L':
    pion(4)
    poziom(5)
else:
    print("Bledna litera")
