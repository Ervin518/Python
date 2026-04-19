import os

def zadanie4():
    foldery = ['StudentDoc', 'StudentObrazy']

    for katalog in foldery:
        if not os.path.exists(katalog):
            os.makedirs(katalog)

        sciezka_txt = os.path.join(katalog, 'notatka.txt')
        plik_txt = open(sciezka_txt, 'w')
        plik_txt.write("Tresc pliku tekstowego.")
        plik_txt.close()
        sciezka_img = os.path.join(katalog, 'obraz.jpg')
        plik_img = open(sciezka_img, 'w')
        plik_img.write("Zalozmy, ze to sa dane obrazka.")
        plik_img.close()
        print("\nZawartosc folderu:", katalog)
        pliki_w_srodku = os.listdir(katalog)

        for p in pliki_w_srodku:
            pelna_sciezka = os.path.join(katalog, p)
            # Sprawdzanie rozmiaru w bajtach
            rozmiar = os.path.getsize(pelna_sciezka)
            print("Plik:", p, "- Rozmiar:", rozmiar, "bajtow")
zadanie4()