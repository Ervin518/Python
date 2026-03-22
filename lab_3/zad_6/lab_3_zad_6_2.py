import lab_3_zad_6_1

n = int(input("Podaj n: "))
k = int(input("Podaj k: "))

if k <= n and k >= 0:
    newton = lab_3_zad_6_1.silnia(n) / (lab_3_zad_6_1.silnia(k) * lab_3_zad_6_1.silnia(n - k))
    print("Symbol Newtona wynosi:", int(newton))
else:
    print("Błędne dane. 'k' musi być większe/równe 0 i mniejsze/równe 'n'.")