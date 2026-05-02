def hasla():
    """
    Funkcja sprawdza poprawnosc hasla podanego przez uzytkownika.
    Haslo musi miec 4-8 znakow, cyfre, mala i wielka litere.
    """
    while True:
        haslo = input("Podaj haslo: ")
        
        if haslo == "":
            print("Haslo nie moze byc puste")
            continue
            
        if len(haslo) < 4 or len(haslo) > 8:
            print("Haslo nie odpowiada potrzebnej dlugosci")
            continue
            
        if not any(char.isupper() for char in haslo):
            print("Nie ma wielkiej litery w hasle")
            continue
            
        if not any(char.islower() for char in haslo):
            print("Nie ma malej litery w hasle")
            continue
            
        if not any(znak.isdigit() for znak in haslo):
            print("Nie ma liczby w hasle")
            continue
            
        with open("haslo.txt", "w", encoding = "UTF-8") as file:
            file.write(haslo)
        print("Haslo zostalo poprawnie zapisane do pliku.")
        break 

hasla()
