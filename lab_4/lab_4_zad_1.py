import random
from operator import sub

list_1 = list(range(1, 101)) 
list_2 = [random.randint(1, 100) for _ in range(100)] 

print(list(map(sub, list_1, list_2)))
