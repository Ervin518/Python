dane = "Jan Kowalski"

rozdziel = lambda tekst: [list(wyraz) for wyraz in tekst.split()]

print("Wynik:", rozdziel(dane))