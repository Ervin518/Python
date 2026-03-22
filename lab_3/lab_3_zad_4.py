loginy = []
hasla = []

while True:
    log = input("Podaj login (lub napisz STOP): ")
    if log == "STOP":
        break
    if log == "":
        print("Login nie może być pusty!")
        continue

    has = input("Podaj hasło: ")

    loginy.append(log)
    hasla.append(has)

baza_danych = {}
for indeks, wartosc_login in enumerate(loginy):
    baza_danych[wartosc_login] = hasla[indeks]

print("Baza danych:", baza_danych)