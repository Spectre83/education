# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# и количества слов в каждой строке.

with open('task_2.txt', 'r') as file_obj:
    file_obj.readlines()
with open('task_2.txt') as file_obj:
    lines = 0
    for line in file_obj:
        lines += 1
        words = len(line.split())
        print(f'{words} слов в линии')
    print(f'строк {lines}')