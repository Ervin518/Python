x = float(input('Podaj ilosc punktow z kolokwium: '))

if 7.5 <= x < 9.15:
    print('3')
elif 9.15 <= x < 10.65:
    print('3.5')
elif 10.65 <= x < 12.15:
    print('4')
elif 12.15 <= x < 13.65:
    print('4.5')
elif 13.65 <= x <= 15:
    print('5')
elif x > 15:
    print('Maksymalna ilosc - 15')
else:
    print('2')