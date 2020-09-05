from itertools import cycle
my_list = ['abc', 212, 21.1, True, False, {'dog': 'Собака', 'cat': 'Кот'}]
n = 0
for el in cycle(my_list):
    if n > 100:
        break
    else:
        print(el)
        n += 1
