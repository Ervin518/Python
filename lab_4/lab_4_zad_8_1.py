import random
from itertools import filterfalse

list_1 = [random.randint(1, 100) for _ in range(100)]

print(list(filterfalse(lambda x: x <= 10 or x % 2 != 0, list_1)))