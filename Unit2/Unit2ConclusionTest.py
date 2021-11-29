# TASK №1
# К новому году для украшения главной елки нужно 1300 стеклянных шариков. Такого количества нет , нужно собрать в разных магазинах.
# В 1 в наличии 250
# 2: 300
# 3:500
# 4:100
# Закупать нужно от максимального, т.е. сначала 500,потом 300, в том где 250 покупаем 200, а 50 в остатке( 1000 уже набрали) А в 4,где их было 100, вообще ничего не покупаем.
# Задача: вывести в каком магазине и сколько купить, в каком магазине останется остаток(в 3 остаток 50), в каком ничего не купим
print('TASK 1')
shop = {1: 350, 2: 400, 3: 600, 4: 100}
a = []
for key in shop:
    a.append(shop[key])
a.sort(reverse=True)
purchase = 0
for i in a:
    for key in shop:
        if shop[key] == i and purchase <= 1300:
            purchase += i
            if purchase <= 1300:
                print("Купить в магазине № ", key, " ", shop[key], 'шаров.')
            else:
                needlessly = purchase - 1300
                print("Купить в магазине № ", key, " ", shop[key] - needlessly, 'шаров', '(там еще останется ', needlessly, ' шаров).')
        elif shop[key] == i and purchase > 1300:
            print('В магазине №', key, ' покупать ничего не нужно.')


# TASK №2
# Вывести сумму всех элементов с1 и с2, наименьшее и наибольшее значение с1 и с2
print('TASK 1')
c1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c2 = (45, 21, 124, 76, 5, 23, 91, 234)
sum1 = 0
for i in c1:
    sum1 += i
print(' sum 1:', sum1)
sum2 = 0
for i in c2:
    sum2 += i
print(' sum 2:', sum2)
print("min1 :", min(c1), 'max1: ', max(c1), 'min2: ', min(c2), 'max2: ', max(c2))


# TASK №3
# Создать словарь, где ключи - символы строки, а значения - число вхождений данного символа в строку
print('TASK 2')
a = "An apple a day keeps the doctor away"
d = {i: a.count(i) for i in a}
print(d)


# TASK №4
print('TASK 3')
# Вывести на экран количество одинаковых элементов в обоих списках
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [6, 7, 8, 9, 10, 11, 12, 13, 14]
c = []
for i in a:
    if i in b:
        c.append(i)
print(len(c))


# TASK №5
# Написать любой пример с использованием try/except.
# Введите два числа через пробел, разделите первое на второе.
# Обработайте исключения деления на ноль и введение пользователем не чисел.
print('TASK 4')
a = (input('Введите любые два числа через пробел: '))
a = a.split(' ')
try:
    int(a[0]) / int(a[1])
except ZeroDivisionError:
    print('ZeroDivisionError')
    a = (input("Второе число не может быть '0', т.к. на ноль делить нельзя. Введите любые два числа через пробел: "))
    a = a.split(' ')
except ValueError:
    print('ValueError')
    a = (input("Неверный ввод. Введите любые два числа через пробел: "))
    a = a.split(' ')
finally:
    print(int(a[0]) / int(a[1]))


# TASK №6
#
# Есть словарь песен группы Depeche Mode
#
# violator

songsdict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# 1.Выведите общее время звучания всех песен.
# 2.Создайте список песен, время звучаниях которых больше 5 минут
# 3.Создайте новый словарь тех песен, в название которых состоит из одного слова
print('TASK 5')
time = 0
longsongs = []
onewordname = []
newdict = {}
for key in songsdict:
    time += songsdict[key]
    a = str(key).split(' ')
    if len(a) == 1:
        onewordname.append(key)
    if songsdict[key] > 5:
        longsongs.append(key)
print('общее длительность всех песен альбома: ', time)
print('песни, длительность которых более 5 минут: ', longsongs)
print('песни с названием из одного слова: ', onewordname)


# TASK №7
# Создайте список, замените первый его элемент на [1, 2, 3],
# затем в конец списка добавьте сумму элементов вложенного списка
print('TASK 6')
a = [1, 2, 3, 4, 5]
a[0] = [1, 2, 3]
a.append(sum(a[0]))
print(a)


# TASK №8
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
print('TASK 7')
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

