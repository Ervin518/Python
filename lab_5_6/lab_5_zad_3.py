def potegi(*args):
    """
    Funkcja oblicza x^x dla kazdego podanego argumentu.
    
    Args:
        *args: Dowolna liczba argumentow.
        
    Returns:
        list: Lista wynikow x^x.
    """
    if len(args) >= 100:
        print("Za duzo argumentow")
    elif len(args) == 0:
        print("Brak argumentow")
    else:
        wyniki = []
        for arg in args:
            try:
                x = float(arg)
                wyniki.append(x ** x)
            except ValueError:
                print("Element '" + str(arg) + "' nie jest liczba. Pomijam.")
        return wyniki

argumenty = input("Podaj argumenty po przecinku: ")
if argumenty.strip() != "":
    wynik_koncowy = argumenty.split(",")
    print("Wyniki: ", potegi(*wynik_koncowy))
else:
    print("Brak argumentow")
