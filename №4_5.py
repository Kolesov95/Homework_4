from functools import reduce
my_list = [el for el in range(100, 1001, 2)]
result = reduce(lambda a, b: a*b, my_list)
print('Результат умножения всех четных чисел от 100 до 1000: {}'.format(result))
