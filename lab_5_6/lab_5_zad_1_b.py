def zmien_katalog(nowa_sciezka):
    os.chdir(nowa_sciezka)
    print("Obecny katalog to:", os.getcwd())
    print("Zawartosc katalogu:")
    print(os.listdir('.'))