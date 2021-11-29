x = open('abc.txt', 'r')
a = x.readlines()
print(a)
b = []
for i in range(len(a)):
    a[i] = a[i].replace('\n', '')
for i in a:
    b.append(i.split(':'))
print(b)
d = dict(b)
d1 = {}
print(d)
spis = []
for key in d:
    spis.append(d[key])
print(spis)
spis.sort()
print(spis)
for i in spis:
x.close()