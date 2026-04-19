import pickle

def zadanie6():
    lista1 = [1, 2, 3]
    lista2 = ['a', 'b', 'c']
    lista3 = [True, False]

    plik_zapis = open('listy.pickle', 'wb')
    pickle.dump((lista1, lista2, lista3), plik_zapis)
    plik_zapis.close()

    del lista1, lista2, lista3

    plik_odczyt = open('listy.pickle', 'rb')
    odczytane = pickle.load(plik_odczyt)
    plik_odczyt.close()

    print("Odczytane z pliku:", odczytane)
zadanie6()
