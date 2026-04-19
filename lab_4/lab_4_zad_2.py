import random
from operator import lt, mod, eq, and_

list_1 = [random.randint(1, 10000) for _ in range(10000)]

mniejsze_i_parzyste = list(
    filter(lambda x: and_(lt(x, 3), eq(mod(x, 2), 0)), list_1)
)

print(mniejsze_i_parzyste)
