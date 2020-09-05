from sys import argv
script_name, hours, rate, award = argv
salary = int(hours) * float(rate) + float(award)
print(f'Выплата сотрудника за месяц: {salary:.2f}')
