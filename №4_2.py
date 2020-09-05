old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(old_list) if old_list[num] > old_list[num-1] and num != 0]
print(f'Старый список: {old_list}')
print(f'Новый список: {new_list}')
