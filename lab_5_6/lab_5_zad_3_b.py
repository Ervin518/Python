import os
import fnmatch


def zadanie3():
    folder = 'Dokument'

    if not os.path.exists(folder):
        os.makedirs(folder)

    nazwy_plikow = ['Lab1.doc', 'Lab2.doc', 'Lab3.doc', 'InnyPlik.txt']
    for nazwa in nazwy_plikow:
        sciezka = os.path.join(folder, nazwa)
        plik = open(sciezka, 'w')
        plik.write("Przykładowy tekst.")
        plik.close()

    wszystkie_pliki = os.listdir(folder)
    print("a) Wszystkie pliki w folderze", folder, ":", wszystkie_pliki)

    print("b) Tylko pliki z rozszerzeniem .doc:")
    for p in wszystkie_pliki:
        if fnmatch.fnmatch(p, '*.doc'):
            print(p)


zadanie3()
