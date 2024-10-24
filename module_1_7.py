grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
k = 0
while k < len(students):
    grades[k] = sum(grades[k])/len(grades[k])
    k += 1
n = 0
dict_ = {}
while n < len(students):
    dict_[students[n]] = grades[n]
    n += 1
print(dict_)
