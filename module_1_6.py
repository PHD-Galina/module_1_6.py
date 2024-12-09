my_dict = {'Laura': 1994, 'Ralina': 1998, 'Kira': 2000}
print('Словарь:', my_dict)
my_dict['Год рождения Лауры:','Laura'] = 1995
my_dict['Irina'] = 2004
print(my_dict.get('Kira'))
print(my_dict.get('Alex'))
my_dict.update({'Misha': 1985,
                'Evelina': 1987})
print(my_dict.get('Melek', 'Такого ключа нет'))
a = my_dict.pop('Irina')
print(my_dict)
print(a)

my_set = {9,7,5,3,1,2,4,6,8,0,'True','False','False', 'True','list'}
print('Множество:', my_set)
my_set.add('orange')
my_set.add('apple')
print(my_set)
my_set.discard(4)
print(my_set)

