def my_sum(**kwargs):
    x = int(input('введите число x: '))
    y = int(input('введите число y: '))
    z = int(input('введите число z: '))
    my_list = [x, y, z]
    my_list.remove(min(my_list))
    print(sum(my_list))
my_sum()

