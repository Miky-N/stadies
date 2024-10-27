n = [7, 5, 4, 1, 6, 3, 0, 3]
b = []
m = ''
k = 0
for i1 in range(len(n)):
    k1 = n.pop(i1)
    for i2 in range(len(n)):
        k2 = n.pop(i2)
        for i3 in range(len(n)):
            k3 = n.pop(i3)
            while k < len(n):
                m = m + str(n[k])
                k += 1
            if int(m)%30==0:
                b.append(m)
            m = ''
            k = 0
            n.insert(i3, k3)
        n.insert(i2, k2)
    n.insert(i1, k1)
print(b)
