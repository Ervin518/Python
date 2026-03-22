poziom = lambda n: print("*" * n)
pion = lambda n: [print("*") for _ in range(n)]

rysuj = lambda lit: (poziom(5), pion(1), poziom(4), pion(1), poziom(5)) if lit.upper() == 'E' else (pion(4), poziom(5)) if lit.upper() == 'L' else print("Błędna litera")

wybor = input("Podaj literę (E lub L): ")
rysuj(wybor)