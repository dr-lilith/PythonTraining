 # TASK №7
#
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
import random

z = []
for i in range(8):
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    z.append((x, y))
print(z)
check = 0
for i in z:
    for u in z:
        if i[0] == u[0] and i[1] != u[1]:
            print('ферзь в положении:', i, 'может побить по вертикали ферзя в положении:', u)
            check = 1

for i in z:
    for u in z:
        if abs(i[1] - u[1] == i[0] - u[0]):
            if i[1] - u[1] != 0 or u[1] - i[1] != 0:
                print('ферзь в положении:', i, 'может побить по диагонали ферзя в положении:', u)
                check = 1
if check == 1:
    print('NO')
else:
    print('YES')