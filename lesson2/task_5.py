my_list = [7, 5, 3, 3, 2]
print(my_list)
number = int(input('Введите целое число: '))
for index, num in enumerate(my_list):
    if number < num:
        continue
    my_list.insert(index, number)
    break
else:
    my_list.append(number)
print(my_list)