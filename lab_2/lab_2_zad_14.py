def iloraz_parzystych(a, b, c):
       return a / b / c if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) and (b != 0 and c != 0) else "Błąd: Liczby nie są parzyste lub wystąpiło dzielenie przez 0"

print(iloraz_parzystych(16, 2, 4))
print(iloraz_parzystych(16, 3, 4))
print(iloraz_parzystych(16, 2, 0))