k = 0
while True:
    my_str = input('введите кучу чисел через пробел или буква "q" для выхода: ')
    numbers = my_str.split(' ')
    for number in numbers:
        try:
            k += int(number)
        except:
            if number == 'q':
                print(f'Результат равен {k}. Программа завершена!')
                exit(0)
            else:
                print('неверный символ! программа завершена!')
                exit(1)
    print(k)
exit()
