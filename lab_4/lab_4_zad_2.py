import random
from operator import lt, mod, eq

list_1 = [random.randint(1, 10001) for _ in range(10000)]

mniejsze_i_parzyste = list(
filter(lambda x: lt(x, 3) and eq(mod(x, 2), 0), list_1)
)

print(mniejsze_i_parzyste)