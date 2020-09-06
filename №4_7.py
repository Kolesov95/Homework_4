from math import factorial


def fact(n):
    for elem in range(1, n+1):
        yield factorial(elem)


generator = fact(int(input('Введите число: ')))
print(generator)
for el in generator:
    print(el)




