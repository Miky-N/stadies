my_dict = {'Olga': 1984, 'Igor': 1981, 'Miky': 2007}
print('Dict:', my_dict)
print('Existing value:', my_dict['Miky'])
print('Not existing value:', my_dict.get('Sasha'))
my_dict.update({'Ncn Ch': 2008, 'Grisha': 1996})
del my_dict['Igor']
print(my_dict.get('Igor', 'This key was deleted (\'Igor\')'))
print(my_dict)

my_set = {1, 3, 3, 'List', 'Apple', 1, False}
print(my_set)
my_set.add(4)
my_set.add(True)
my_set.remove(3)
print(my_set)