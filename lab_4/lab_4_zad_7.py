import operator
from itertools import accumulate

def oblicz_lokate():
    kwota_poczatkowa = 10000
    # 0.01% to matematycznie 0.0001
    oprocentowanie = 0.0001
    mnozniki = [kwota_poczatkowa] + [1 + oprocentowanie] * 3
    historia_kwot = list(accumulate(mnozniki, operator.mul))
    return historia_kwot[-1]

print("Kwota po 9 miesiacach:", oblicz_lokate())
