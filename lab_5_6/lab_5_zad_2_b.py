def zmien_katalog(nowa_sciezka):
    os.chdir(nowa_sciezka)
    print("Obecny katalog to:", os.getcwd())
    print("Zawartosc katalogu:")
    print(os.listdir('.'))

def zadanie2():
    while True:
        odpowiedz = input("Czy mam zmienic katalog? (wpisz 'yes'): ")

        if odpowiedz == "yes":
            sciezka = input("Podaj pelna sciezke do katalogu (np. C:\\Windows): ")
            zmien_katalog(sciezka)
            break
        else:
            print("Musisz wpisac 'yes'!")

zadanie2()