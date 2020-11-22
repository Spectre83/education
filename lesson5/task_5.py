# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('task_5.txt', 'w+', encoding='utf-8') as file_obj:
            str = input('Введите цифры через пробел: ')
            file_obj.writelines(str)
            numb = str.split()
            print(sum(map(int, numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно введено число!')
summary()