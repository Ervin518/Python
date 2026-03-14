a = int(input('Podaj liczbe: '))

if a % 2 == 0 and a != 0:
    print('Parzysta')
elif a % 2 == 1:
    print('Nieparzysta')
elif a == 0:
    print('Ani parzysta, ani nieparzysta')