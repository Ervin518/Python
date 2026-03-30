from itertools import combinations

n = int(input("Podaj liczbe studentow: "))
a = int(input("Podaj liczbe podgrup: "))
list_1 = list(range(1, n+1))

print(list(combinations(list_1,a)))