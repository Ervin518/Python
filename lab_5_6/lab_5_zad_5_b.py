import os

def zadanie5():
    stara_nazwa = 'StaryKatalog'
    nowa_nazwa = 'NowyKatalog'

    if not os.path.exists(stara_nazwa):
        os.makedirs(stara_nazwa)

    if not os.path.exists(nowa_nazwa):
        os.rename(stara_nazwa, nowa_nazwa)
        print("\nZmieniono nazwe folderu z", stara_nazwa, "na", nowa_nazwa)

zadanie5()