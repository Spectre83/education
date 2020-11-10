goods = []
features = {'название': '', 'цена': '', 'кол-во': '', 'ед.изм.': ''}
analytics = {'название': [], 'цена': [], 'кол-во': [], 'ед.изм.': []}
num = 0
feature_ = None
control = None
while True:
    control = input('Для выхода введите "Q", для продолжения нажмите "Enter", для аналитики введита "A" ').upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        for key, value in analytics.items():
            print(f'{key}: {value}')
    for f in features.keys():
        feature_ = input(f'ВВедите данные "{f}" ')
        features[f] = int(feature_) if (f == 'цена' or f == 'кол-во') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({'название': input("введите название товара: "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)
