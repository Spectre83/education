my_string = input('введите строку: ')
words = []
number = 1
for elem in range(my_string.count(' ') + 1):
    words = my_string.split()
    if len(str(words)) <= 10:
        print(f' {number} {words [elem]}')
        number += 1
    else:
        print(f' {number} {words [elem] [0:10]}')
        number += 1