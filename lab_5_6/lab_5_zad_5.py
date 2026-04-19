import os

if not os.path.exists('Lab_5_zad5'):
    os.mkdir('Lab_5_zad5')
path = os.path.join('Lab_5_zad5', 'Text1ID_ABC.txt')
with open(path, 'w') as file:
    file.write('Jestem z Bialorusi. Nazywam sie Erwin. Mam 18 lat, 2008 rok urodzenia. Bardzo kocham swoj kraj. Mnie bardzo podoba sie w Polsce')
path = os.path.join('Lab_5_zad5', 'Text2ID_405.txt')
with open(path, 'w') as file:
    file.write("I'm from Belarus. My name is Erwin. I'm 18 years old and was born in 2008. I love my country very much. I really like Poland.")
path = os.path.join('Lab_5_zad5', 'Text3ID_607.txt')
with open(path, 'w') as file:
    file.write('Я з Беларусі. Мяне завуць Эрвін. Мне 18 гадоў, я нарадзіўся ў 2008 годзе. Я вельмі люблю сваю краіну. Мне вельмі падабаецца Польшча.')
path = os.path.join('Lab_5_zad5', 'Text4ID_ABC5.txt')
with open(path, 'w') as file:
    file.write('Я из Беларуси. Меня зовут Эрвин. Мне 18 лет, я родился в 2008 году. Я очень люблю свою страну. Мне очень нравится Польша.')
path = os.path.join('Lab_5_zad5', 'Text5ID_DEF.txt')
with open(path, 'w') as file:
    file.write('Я з Білорусі. Мене звати Ервін. Мені 18 років, я народився у 2008 році. Я дуже люблю свою країну. Мені дуже подобається Польща.')

def dekorator(funkcja):
    """
    Dekorator zlicza pliki z cyfra '0' i kopiuje pliki z 'EF.txt'.
    """
    def wrapper(*args):
        funkcja(*args)
        folder = args[0]
        pliki = os.listdir(folder)
        ile_z_zerem = 0
        for nazwa in pliki:
            sciezka = os.path.join(folder, nazwa)
            if '0' in nazwa:
                ile_z_zerem += 1
                with open(sciezka, 'r') as file:
                    text = file.read()
                    slowa = text.split()
                    print("Plik", nazwa, "ma slow:", len(slowa))
            if 'EF.txt' in nazwa:
                nowy_folder = 'DocumentLab5copy'
                if not os.path.exists(nowy_folder):
                    os.mkdir(nowy_folder)
                nowa_sciezka = os.path.join(nowy_folder, nazwa)
                
                with open(sciezka, 'r') as stary:
                    tresc = stary.read()
                with open(nowa_sciezka, 'w') as nowy:
                    nowy.write(tresc)
                print('Skopiowano plik', nazwa, "do", nowy_folder)
                
        print("Liczba plikow z '0':", ile_z_zerem)
    return wrapper

@dekorator
def files(*args):
    """
    Funkcja wypisuje wszystkie pliki i analizuje zawartosc plikow z 'ABC'.
    """
    folder = args[0]
    try:
        pliki = os.listdir(folder)

        print("Wszystkie pliki w folderze:")
        print(pliki)

        for nazwa in pliki:
            if 'ABC' in nazwa:
                sciezka = os.path.join(folder, nazwa)
                with open(sciezka, 'r') as file:
                    tekst = file.read()
                    slowa = tekst.split()
                    licznik = 0
                    for s in slowa:
                        if len(s) > 3:
                            licznik += 1
                    print("Plik", nazwa, "ma", licznik, "slow dluzszych niz 3 litery.")
    except Exception as e:
        print("Blad:", e)

files("Lab_5_zad5")
