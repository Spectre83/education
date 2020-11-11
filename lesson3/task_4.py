# 1-й вар.

x = int(input('введите число x: '))
y = int(input('введите число y: '))
def my_func(x, y):
    z = x**y
    return z
print(my_func(x, y))

# 2-й вар.

def my_func(x, y):
    z = 1
    for i in range(abs(y)):
        z *= x
    return 1 / z
print(my_func(x, y))