import functools

list_word = ['E', 'r', 'v', 'i', 'n']
imie = functools.reduce(lambda x, y: x + y, list_word)

print("Moje imie:", imie)
