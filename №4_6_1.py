from itertools import count
user_request = int(input('Введите число, с которого начнется генерация чисел: '))
for i in count(user_request):
    if i > user_request + 100:
        break
    else:
        print(i)
