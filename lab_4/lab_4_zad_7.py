import operator
from itertools import accumulate

kwota_poczatkowa = 10000
oprocentowanie = 0.001
miesiace = 9
okresy_miesiacу = miesiace // 3

mnozniki = [kwota_poczatkowa] + [1 + oprocentowanie] * okresy_miesiacу

list_1 = list(accumulate(mnozniki, operator.mul))

print("Wyniki kwoty to ", list_1[-1])

