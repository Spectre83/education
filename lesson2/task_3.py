# решение через список.

seasons = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input('Введите номер месяца от 1 до 12: '))
if month == 1 or month == 2 or month == 12:
        print(seasons[0])
elif month == 3 or month == 4 or month == 5:
        print(seasons[1])
elif month == 6 or month == 7 or month == 8:
        print(seasons[2])
elif month == 9 or month == 10 or month == 11:
        print(seasons[3])
else:
    print('Нет такого месяца!')

# решение через словарь.

seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
month_number = int(input('Введите номер месяца от 1 до 12: '))
for key in seasons.keys():
    if month_number in seasons[key]:
        print(key)