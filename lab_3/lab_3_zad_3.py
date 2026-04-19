szukaj_litery = lambda wyraz, litera: print('Jest taka litera') if litera in wyraz else print('Nie ma takiej litery')

a = input('Podaj dowolny wyraz: ')
b = input('Podaj dowolna litere: ')

szukaj_litery(a, b)
