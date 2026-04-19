import os


def przygotuj_pliki_zad9():
    pliki = [
        'Tekst1ID_ABC.txt',
        'Tekst2ID_405.txt',
        'Tekst3ID_607.txt',
        'Tekst4ID_ABC.txt',
        'Tekst5ID_DEF.txt'
    ]
    tresc = "To jest pierwsze zdanie. Programowanie to super sprawa. Robimy zadanie z Pythona. Otwieramy i zamykamy pliki. Dzis jest dobry dzien."

    for nazwa in pliki:
        plik = open(nazwa, 'w', encoding='utf-8')
        plik.write(tresc)
        plik.close()


def funkcja_bazowa():
    katalog = '.'
    wszystkie_pliki = os.listdir(katalog)

    for p in wszystkie_pliki:
        if 'ABC' in p and p.endswith('.txt'):
            plik = open(p, 'r', encoding='utf-8')
            tekst = plik.read()
            plik.close()

            slowa = tekst.split()
            licznik_dlugich = 0
            for s in slowa:
                if len(s) > 3:
                    licznik_dlugich = licznik_dlugich + 1

            print("W pliku", p, "znaleziono", licznik_dlugich, "slow(a) dluzszych niz 3 litery.")

    return wszystkie_pliki


def funkcja_dodatkowa():
    lista_plikow = funkcja_bazowa()

    licznik_plikow_z_zerem = 0

    for p in lista_plikow:
        if 'Tekst' in p and p.endswith('.txt'):
            if '0' in p:
                licznik_plikow_z_zerem = licznik_plikow_z_zerem + 1
            else:
                plik = open(p, 'r', encoding='utf-8')
                tekst = plik.read()
                plik.close()

                wszystkie_slowa = tekst.split()
                print("Plik BEZ cyfry '0' (", p, ") ma lacznie", len(wszystkie_slowa), "slow.")

    print("Laczna liczba plikow zawierajacych '0' w nazwie:", licznik_plikow_z_zerem)


przygotuj_pliki_zad9()
funkcja_dodatkowa()