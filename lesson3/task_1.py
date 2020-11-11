a = int(input('введите число а: '))
b = int(input('введите число b: '))
def my_func(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print('деление на ноль!')
    except ValueError:
        print('допустимы только числа!')
print(my_func(a, b))