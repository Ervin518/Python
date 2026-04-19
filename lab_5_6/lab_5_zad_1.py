from operator import ge, le

def hasla():

    while True:
        haslo = input("Podaj haslo: ")
        if haslo == "":
            print("Haslo nie moze byc puste")
            break
        if not ge(len(haslo), 4) and le(len(haslo), 8):
            print("Haslo nie odpowiada potrzebnej dlugosci")
            break
        if not any(char.isupper() for char in haslo):
            print("Nie ma wielkiej litery w hasle")
            break
        if not any(char.islower() for char in haslo):
            print("Nie ma malej litery w hasle")
            break
        if not any(znak.isdigit() for znak in haslo):
            print("Nie ma liczby w hasle")
            break
        break

dane = haslo

with open("haslo.txt", "w", encoding = "UTF-8") as file:
    file.write(dane)