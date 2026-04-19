from struct import pack, unpack

def zadanie7():
    liczba = 123456789

    spakowana = pack('i', liczba)

    plik1 = open('liczba.dat', 'wb')
    plik1.write(spakowana)
    plik1.close()

    plik2 = open('liczba.dat', 'rb')
    dane = plik2.read()
    plik2.close()

    rozpakowana = unpack('i', dane)
    print("Rozpakowana liczba to:", rozpakowana[0])


zadanie7()
