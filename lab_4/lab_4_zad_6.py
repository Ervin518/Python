from itertools import combinations

def podzial_na_grupy(N, rozmiar_grupy):
    studenci = list(range(1, n+1))
    return list(combinations(studenci, rozmiar_grupy))
n = int(input("Podaj laczna liczbe studentow (N): "))
a = int(input("Podaj rozmiar podgrupy: "))
print(podzial_na_grupy(n, a))
