immutable_var = ('apple', 2, True)
print(immutable_var, '- a Tuple, cannot be changed')
#immutable_var[0] = 'Apple' выводит ошибку
mutable_list = ['apple', 2, True, 'non-modified']
print(mutable_list, '- a List')
mutable_list[-1] = 'Modified'
print(mutable_list)