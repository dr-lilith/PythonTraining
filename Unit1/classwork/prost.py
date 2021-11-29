# string = input("Введите строку, состоящую из прописных и строчных латинских букв:")
# stringList = list(string)
# vowels = ["e", "y", "u", "i", "o", "a", "E", "Y", "U", "O", "A", "I"]
# for i in range(1, len(stringList)):
#     if stringList[i] in vowels:
#         stringList.pop(i)
#     else:
#         stringList[i - 1] = "."
# if stringList[0] in vowels:
#     stringList.pop(0)
# else:
#     stringList.insert(0, '.')
# print(stringList)


#  classwork 27/10/21
# elements = [1, 3, 6, "a", "b", "abc", 123, 435]
# if "abc" in elements:
#     print("yes")

# d = ['h',  'e',  'l',  'l',  'o']
# e = ['w', 'o', 'r', 'l', 'd']
# print(d + e)
# d.extend(e)
# print(d)
# print(e)

# print("Игра крестики-нолики:")
# # ourList = [" -------------\n", [["| "], 1, [' | '], 2, [' | '], 3, [' |\n']],
# #            [["| "], 4, [' | '], 5, [' | '], 6, [' |\n']], ["| "], [7, [' | '], 8, [' | '], 9, [' |\n']],
# #            "-------------\n"]
# # print(*ourList, sep='\n')
#
# first = [1, 2, 3]
# second = [4, 5, 6]
# third = [7, 8, 9]
# print(first, "\n", second, "\n", third)
# print("Вместо выбранной Вами цифры будет ставиться крестик + ")
# for i in range(10):
#     a = int(input("Сделайте выбор, напишите цифру:"))
#     if a in first:
#         if a == 1:
#             first[0] = "+"
#         elif a == 2:
#             first[1] = "+"
#         elif a == 3:
#             first[2] = "+"
#     elif a in second:
#         if a == 4:
#             second[0] = "+"
#         elif a == 5:
#             second[1] = "+"
#         elif a == 6:
#             second[2] = "+"
#     elif a in third:
#         if a == 7:
#             third[0] = "+"
#         elif a == 8:
#             third[1] = "+"
#         elif a == 9:
#             third[2] = "+"
#     string1 = ' '.join(str(first))
#     print(string1, "\n", ' '.join(str(second)), "\n", ' '.join(str(third)))

#
# a = (1,)
# print(a.__sizeof__())
#
# # a = [1,2,3,4,5,6,7]
# # a.reverse()
# # print(a)
#
# a = [2, 3, 6, 20, 40, 20, 80]
# b = a.index(20)
# print(b)
# a[b] = 200
# print(a)

# a = [5, [1, 2], 2, "r", 4, 'ee']
# b = [4, "we", "ee", 3, [1, 2]]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# a = [4, 6, "py", 'tell', 78]
# b = [44, "hello", 56, "exept", 3]
# print(a + b)
# a.extend(b)
# a.insert(3,6)
# print(a)
# for i in a:
#     if type(i) is str:
#         a.remove(i)
# a.sort()
# print(a)

# a = (1, 2, 3, "go", [2,3,4])
# a[4][2] = 15
# print(a)


# import random
# a = [random.randint(0,100) for i in range(10)]
# b = tuple(a)
# print(b)


# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(sum(a))
#
# long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
# b = long_word.count('т')
# c = long_word.count('а')
# d = long_word.count('и')
# print('букв т:', b, 'букв а:', c, 'букв и:', d)
#
# week_temp = (26, 29, 34, 32, 28, 26, 23)
# sum_temp = sum(week_temp)
# days = len(week_temp)
# mean_temp = sum_temp / days
# print(int(mean_temp))

import random
# o = 0
# f = []
# while o < 10:
#     o += 1
#     f.append(random.randint(0,100))
# y = tuple(f)
# print(y)
# print('min = {0}, max = {1}'.format(min(y), max(y)))


# g = tuple([random.randint(0,5) for i in range(10)])
# j = tuple([random.randint(-5,0) for i in range(10)])
# k = g + j
#
# print(k, '\n Количество нулей: ', k.count(0))


# s = ('лорп', 'ьотр', 'торп', 'орп')
# d = ','.join(s)
# print(type(d))
# print(d)


# b = (6,8,4,5,3,2,9,0,6,5,7)
# c = (7,4,5,2,4,9,7,8,6,5)
# print(sum(b), sum(c), b.index(max(b)), b.index(min(b)), max(c), min(c))

# r = ('р','р','р','д','д','д','д','д','д','в','в','в','в','в','в','в','к','к','к','к','к','к','к')
# print(r.count('р'), r.count('д'), r.count('в'), r.count('к'), r.count('р'))

# weekTemp = (28,29,27,26,29,27,29)
# sumTemp = sum(weekTemp)

# days = len(weekTemp)
# meanTemp = sumTemp / days
# print(int(meanTemp))



# d = dict(zip(['apple', 'candy', 'tomato', 'juice', 'ice cream', 'tea'],[[1,30], [2,25], [1,23], [2,24], [3,20], [4,15]]))
# print(d)
# print("наличие на складе:")
# for key in d:
#      print(key, " - цена: ", d[key][0], ' - количество на складе: ', d[key][1])
# a = input('введите нужный Вам товар:')
# while a not in d:
#      print('такой товар не найден')
#      a = input('введите нужный Вам товар из имеющихся на складе:')
# b = int(input('введите его количество:'))
# while b > d[a][1]:
#      print('на складе недостаточное количество товара, max для заказа: ', d[a][1])
#      b = int(input('введите его количество, доступное для заказа:'))
# print("ваша цена: ", b * d[a][0])
# print("на складе осталось данных позиций: ", d[a][1] - b)

# a = ['jhgf', 'oiuytre', 'poiuytrew']
# vowels = ['a', 'e', 'y', 'u', 'i', 'o']
# d = {}
# for i in a:
#      for l in i:
#           if l in vowels:
#                d[l] = l
# print(len(d))
#
# s = ['jhgdcf', 'jhgfd']
# t = ['jhnbfgf', 'joiuhgfd']
# j = ['jytrhgf', 'jhgfytd']
# p = ['jhjhggf', 'jhgkjhfd']
# d = s+t
# q = j + p
# f = dict(zip(d,q))
# print(f)
# try:
#      a = 1/0
# except BaseException:
#      a = 0
# print(a)
#
# d = {'a':1, 'b':2, 'c':3}
# try:
#      value = d['d']
# except KeyError:
#      print("ключа не существует")
# else:
#     print("ошибок нет")

# pencilSet = {'red', 'blue', 'violet', 'black', 'yellow', 'green'}
# b = []
# print(pencilSet)
# i = 0
# while i < 6:
#     a = input('choose the colour of the pencil: ')
#     if a in pencilSet:
#         b.append(a)
#         pencilSet.discard(a)
#         print(pencilSet)
#     else:
#         print('has been taken')
# #     i += 1

# import logging
# import math
#
# a, b, c = None, None, math.inf
# while a is None or b is None:
#     try:
#         a = int(input('Input dividable: '))
#         b = int(input('Input divider: '))
#     except ValueError:
#         print('Invalid input')
#         continue
#
# try:
#     c = a // b
# except ZeroDivisionError:
#     None
#     #logging.exception("Zero division")
# except ArithmeticError:
#     logging.exception("Arithmetic error")
# finally:
#     print('Division result: ', c)


# string = input('Введите строку: ')
# a = string.split()
# d = {}
# for i in a:
#     d[i] = a.count(i)
# print(d)

# print(a, type(a))
# for i in a:
#     if i[-1].isalpha() == False:
#         b.append(i[:-1])
#     else:
#         b.append(i)
# print(b)


# ourset = {1,2,3,4,5}
# ourfrosenset = frozenset(ourset)
# print(ourfrosenset)

# Для украшения зала нужно 1000 зелёных шариков. Такого количества нет , нужно собрать в разных магазинах.
# В 1 в наличии 250
# 2: 300
# 3:500
# 4:100
# Закупать нужно от максимального, т.е. сначала 500,потом 300, в том где 250 покупаем 200, а 50 в остатке( 1000 уже набрали) А в 4,где их было 100, вообще ничего не покупаем.
# Задача: вывести в каком магазине и сколько купить, в каком магазине останется остаток(в 3 остаток 50), в каком ничего не купим

# shop = {1: 250, 2: 300, 3: 500, 4: 100}
# a = []
# for key in shop:
#     a.append(shop[key])
# a.sort(reverse=True)
# purchase = 0
# for i in a:
#     for key in shop:
#         if shop[key] == i and purchase < 1000:
#             purchase += i
#             if purchase <= 1000:
#                 print("Купить в магазине № ", key, " ", shop[key], 'шаров.')
#             else:
#                 needlessly = purchase - 1000
#                 print("Купить в магазине № ", key, " ", shop[key] - needlessly, 'шаров', '(там еще останется ', needlessly, ' шаров).')
#         elif shop[key] == i and purchase >= 1000:
#             print('В магазине №', key, ' покупать ничего не нужно.')


# ПЕРВАЯ:

# В саду сорвали цветы
# garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
# На лугу сорвали цветы
# meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
# Создайте множество цветов, произрастающих в саду и на лугу

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)
flowers = set()
for i in garden:
    flowers.add(i)
for t in meadow:
    flowers.add(t)
print(flowers)


# ВТОРАЯ

# Есть словарь песен группы Depeche Mode
# violator
# songsdict = {
# 'World in My Eyes': 4.76,
# 'Sweetest Perfection': 5.43,
# 'Personal Jesus': 4.56,
# 'Halo': 4.30,
# 'Waiting for the Night': 6.07,
# 'Enjoy the Silence': 4.6,
# 'Policy of Truth': 4.88,
# 'Blue Dress': 4.18,
# 'Clean': 5.68,
# }
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь их песен, в название которых состоит из одного слова

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
print('общее длительность всех песен альбома: ',time)
print('песни, длительность которых более 5 минут: ', longsongs)
print('песни с названием из одного слова: ', onewordname)


# Numbers = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
# print(Numbers)
# person = {'name': "Ira", 'age': 25, 'city': 'Minsk'}
# print(person['age'])
#
# cars = {"BMW": ['a1', 'a2', 'a3'], "Tesla": ['d6', 'd7', 'd8']}
# print(cars['BMW'][0], cars['BMW'][-1], cars['Tesla'][0], cars['Tesla'][-1])
# a = {'b': 2, 'c': 3, 'd': 4}
# print(a['b'] * a['c'] * a['d'])
# res = 1
# for key in a:
#     res *= a[key]
# print(res)
# slovar = dict(zip(['one', 'two', 'three', 'four', 'five'], [1, 2, 3, 4, 5]))
# print(slovar)
# l = {}
# for i in "pythonist":
#     if i not in l:
#         l[i] = 1
#     else:
#         l[i] += 1
# print(l)

# SHOP

# d = dict(zip(['apple', 'candy', 'tomato', 'juice', 'ice cream', 'tea'],
# #              [[1, 30], [2, 25], [1, 23], [2, 24], [3, 20], [4, 15]]))
# # # for key, value in d.items():
# # #     print()
# # print("наличие на складе:")
# # for key in d:
# #     print(key, " - цена: ", d[key][0], ' - количество на складе: ', d[key][1])
# # vibor = "yes"
# # while vibor == 'yes':
# #     a = input('введите нужный Вам товар:')
# #     while a not in d:
# #         print('такой товар не найден')
# #         a = input('введите нужный Вам товар из имеющихся на складе:')
# #     b = int(input('введите его количество:'))
# #     while b > d[a][1]:
# #         print('на складе недостаточное количество товара, max для заказа: ', d[a][1])
# #         b = int(input('введите его количество, доступное для заказа:'))
# #     print("ваша цена: ", b * d[a][0])
# #     print("на складе осталось данных позиций: ", d[a][1] - b)
# #     vibor = input("введите 'yes', если хотите продолжить покупки: ")


# print(
#     "ЭТО ИГРА КРЕСТИКИ-НОЛИКИ. ПОБЕЖДАЕТ ТОТ, КТО ПЕРВЫМ УСПЕЛ ЗАНЯТЬ ПОЛНОСТЬЮ ДИАГОНАЛЬ ИЛИ ЛИНИЮ.\nВыбор делается,"
#     " как в морском бою(например, a1 или с3)")
# c = [['      1 ', ' 2 ', ' 3 '], [' a ', " * ", ' * ', ' * '], [' b ', " * ", ' * ', ' * '],
#      [' c ', " * ", ' * ', ' * ']]
#
#
# def game():
#     print(str(c[0][0]), str(c[0][1]), str(c[0][2]), '\n', str(c[1][0]), str(c[1][1]), str(c[1][2]),
#           str(c[1][3]), '\n', str(c[2][0]), str(c[2][1]), str(c[2][2]), str(c[2][3]), '\n', str(c[3][0]), str(c[3][1]),
#           str(c[3][2]), str(c[3][3]))
#
# def first():
#     if hod1[0] == "a":
#         if hod1[1] == '1':
#             c[1][1] = ' + '
#         elif hod1[1] == '2':
#             c[1][2] = ' + '
#         elif hod1[1] == '3':
#             c[1][3] = ' + '
#     elif hod1[0] == "b":
#         if hod1[1] == '1':
#             c[2][1] = ' + '
#         elif hod1[1] == '2':
#             c[2][2] = ' + '
#         elif hod1[1] == '3':
#             c[2][3] = ' + '
#     elif hod1[0] == "c":
#         if hod1[1] == '1':
#             c[3][1] = ' + '
#         elif hod1[1] == '2':
#             c[3][2] = ' + '
#         elif hod1[1] == '3':
#             c[3][3] = ' + '
#
# def second():
#       if hod2[0] == "a":
#           if hod2[1] == '1':
#               c[1][1] = ' o '
#           elif hod2[1] == '2':
#               c[1][2] = ' o '
#           elif hod2[1] == '3':
#               c[1][3] = ' o '
#       elif hod2[0] == "b":
#           if hod2[1] == '1':
#               c[2][1] = ' o '
#           elif hod2[1] == '2':
#               c[2][2] = ' o '
#           elif hod2[1] == '3':
#               c[2][3] = ' o '
#       elif hod2[0] == "c":
#           if hod2[1] == '1':
#               c[3][1] = ' o '
#           elif hod2[1] == '2':
#               c[3][2] = ' o '
#           elif hod2[1] == '3':
#               c[3][3] = ' o '
#
# def check_victory():
#     if c[1][1] == c[1][2] == c[1][3] != " * " or c[2][1] == c[2][2] == c[2][3] != " * " or c[3][1] == c[3][2] == \
#             c[3][3] != " * " or c[1][1] == c[2][1] == c[3][1] != " * " or c[1][2] == c[2][2] == c[3][2] != " * " or \
#             c[1][3] == c[2][3] == c[3][3] != " * " or c[1][1] == c[2][2] == c[3][3] != " * " or c[1][3] == c[2][
#         2] == c[3][1] != " * ":
#         print("ПОБЕДА!")
#         return True
#
# game()
#
# while True:
#     hod1 = input("Игрок номер 1, вы играете крестиками 'x'. Ваш ход: ")
#     first()
#     game()
#     if check_victory():
#         break
#     hod2 = input("Игрок номер 2, вы играете ноликами 'o'. Ваш ход: ")
#     second()
#     game()
#     if check_victory():
#         break
#
# f = open('example.txt', 'r')
# print(*f)
# print(f)
# f.close()
# with open('example.txt') as f:
#     print(*f)
# f = open('example.txt', 'r')
# print(f.read(7))
# f.close()
#
# x = open('example.txt', 'r')
# print(x.readline()) #первая
# print(x.readline())   #вторая
# print(x.readlines())  #все строки список строк
# f = open('xyz.txt', 'w')
# f.write('Hello \nWorld')
# f.close()
#
# import os
# os.rename("xyz.txt", 'abc.txt')
# print('Текущая директория: ', os.getcwd())
# os.mkdir("folder")
# os.chdir("folder")
# os.chdir("..")
# os.makedirs("nested1/nested2/nested3")
# os.rmdir("folder")
# os.removedirs("nested1/nested2/nested3")


# print("Текущая директория изменилась на  folder: ", os.detcwd(folder))
#


# Domashks
# x = open('abc.txt', 'r')
# a = x.readlines()
# print(a)
# digits = []
# words = []
# for i in a:
#     try:
#         b = int(i)
#         digits.append(b)
#     except ValueError:
#         print("not number")
#         words.append(i)
# print(digits)
# digits.sort()
# print(digits)
# # print(words)
# # words.sort()
# print(words)
# wordsort = []
# for i in words:
#     for f in words:
#         if len(i) <= len[0] and len(i) <= len[1] and len(i) <= len[2]:
#             wordsort.append(i)
# print(wordsort)
# all = digits + wordsort
#
#
#     i = i.replace('_', ' ')
#     l = i.split(" ")
# print(l)
# sum = 0
# for i in l:
#     if i.isdigit():
#         i = int(i)
#         sum += i
# print(sum)
# print(a[0])
#
# x.close()

# import random
# list_1 =[]
# for i in range(11):
#     l=random.randint(1,10)
#     list_1.append(l)
# print(list_1)
# s=[]
# for l in list_1:
#     if list_1.count(l) ==1:
#         s.append(l)
# print(s)
# s.sort(reverse=True)
# print(s)
# d=dict.fromkeys(s,1)
# print(d)

# import random
#
# n = int(input("Введите размерность квадрата: "))
# a = set()
# b1 = []
# b2 = []
# b3 = []
# while len(a) == n ** 2:
#         t = random.randint(1, n ** 2)
#         a.add(t)
# print(a)
# while len(b1) == n:
#     b1.append(a.pop())
#     b2.append(a.pop())
#     b3.append(a.pop())
# print(b1, '\n', b2, '\n', b3)


# shop = [("apples, 25"), ('bananas, 20'), ("pears, 15"), ('grape, 26'), ('apples, 25'), ('pinapples, 31'), ("apricots, 30"), ("peaches, 29")]
# shopset = set(shop)
# listshopset = list(shopset)
# for i in shop:
#     if i not in listshopset:
#         print(i)


# К новому году для украшения главной елки нужно 1300 стеклянных шариков. Такого количества нет , нужно собрать в разных магазинах.
# В 1 в наличии 250
# 2: 300
# 3:500
# 4:100
# Закупать нужно от максимального, т.е. сначала 500,потом 300, в том где 250 покупаем 200, а 50 в остатке( 1000 уже набрали) А в 4,где их было 100, вообще ничего не покупаем.
# Задача: вывести в каком магазине и сколько купить, в каком магазине останется остаток(в 3 остаток 50), в каком ничего не купим
# shop = {1: 350, 2: 400, 3: 600, 4: 100}
# a = []
# for key in shop:
#     a.append(shop[key])
# a.sort(reverse=True)
# purchase = 0
# for i in a:
#     for key in shop:
#         if shop[key] == i and purchase <= 1300:
#             purchase += i
#             if purchase <= 1300:
#                 print("Купить в магазине № ", key, " ", shop[key], 'шаров.')
#             else:
#                 needlessly = purchase - 1300
#                 print("Купить в магазине № ", key, " ", shop[key] - needlessly, 'шаров', '(там еще останется ', needlessly, ' шаров).')
#         elif shop[key] == i and purchase > 1300:
#             print('В магазине №', key, ' покупать ничего не нужно.')

# x = open('classwork1311', 'r')
# a = ['g', 'gf', 43, 765, 987, 43, 'kjh', 'jhggf']
# c = []
# for i in a:
#     try:
#         b = int(i)
#     except ValueError:
#         print()
#     else:
#         c.append(b)
#         a.remove(i)
# print(a)
# print(c)
# c.sort()
# print(c)
# d = a + c
# for i in d:
#     x.write(i)
# x.close()

# text = x.readlines()
# size = len(text)
# print('количество строк:', size)
# for i in text:
#     print('длинна строки', len(i))

# if input = ''
# break

# a = x.readlines()
# print(a)
# digits = []
# words = []
# for i in a:
#     try:
#         b = int(i)
#         digits.append(b)
#     except ValueError:
#         print("not number")
#         words.append(i)
# print(digits)
# digits.sort()
# print(digits)
# # print(words)
# # words.sort()
# print(words)
# wordsort = []
# for i in words:
#     for f in words:
#         if len(i) <= len[0] and len(i) <= len[1] and len(i) <= len[2]:
#             wordsort.append(i)
# print(wordsort)
# all = digits + wordsort

# a = {[1,2,3], ['jh', 'jhygt']}
# print(a, type(a))

# a[0][0] = 123
# print(a, type(a))

# a = (input())
# a = a.split(' ')
# try:
#     int(a[0])/int(a[1])
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#     a = (input())
#     a = a.split(' ')
# except ValueError:
#     print('ValueError')
#     a = (input())
#     a = a.split(' ')
# finally:
#     print(int(a[0]) / int(a[1]))
#
#
# x = open('abc.txt', 'r')
# lines = x.readlines()
# print(lines)
# for i in range(len(lines)):
#     # b.append(i, end='')
#     # print(i, end='')
#     lines[i] = lines[i].replace('\n', '')
# print(lines)
# digits = []
# words = []
# for item in lines:
#     if item.isnumeric():
#         digits.append(int(item))
#     else:
#         words.append(item)
# print(digits)
# digits.sort()
# print(digits)
# print(words)
# lens = []
# wordsort = []
# for word in words:
# #     wordlens.append((word, len(word)))
# # wordlens.sort(key=lambda l: l[1])
#     lens.append(len(word))
# print(lens)
# # for word in words:
# for item in lens:
#     # for item in lens:
#     for word in words:
#
#
#         if item == min(lens) and item != 100:
#             wordsort.append(words[lens.index(item)])
#             item = 100
#
# print(wordsort)
# # all = digits + wordsort


# a = [2,3,4,5,6,2,3,4,5,6,7]
# a=[1,1,2,2,1,2]
# # a=[1,1,2,2,1,2,4,5,5,5,5]
# c = set(a)
# pair = 0
# for i in c:
#     b = a.count(i)
#     pair += b//2
# print(pair)
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)


# a = 'jhg ,hgfd) !jhg.'
# print(a)
# sym = ['.', ',', '!', '-', '&', '?', ' ', '(', ')']
# for i in a:
#     if i in sym:
#         a = a.replace(i, '_')
# print(a)
# a = a.split('_')
# print(a)
# for i in a:
#     if i == '':
#         a.remove(i)
# print(a)


# d = dict(zip(['cake', 'candy', 'maffin'],
#              [[['sostav'], 20, 234], [['sostav'], 15, 168], [['sostav'], 17, 206]]))
# print(d)
#
# a = input('введите нужный Вам товар:')
# while a not in d:
#     print('такой товар не найден')
#     a = input('введите нужный Вам товар из имеющихся на складе:')
# for key in d:
#     if key == a:
#         y = int(input(
#             "Введите цифру для выбора одной из возможных функций: 1) посмотреть описание, 2) посмотреть цену, 3) посмотреть количество, 4) всю инфу, 5) приступить к покупке, 6) до свидания"))
#         if y == 1:
#             print(key, ' - ', d[key][0])
#         elif y == 2:
#             print(key, ' - ', d[key][1])
#         elif y == 3:
#             print(key, ' - ', d[key][2])
#         elif y == 4:
#             print(key, ' - ', d[key][0], d[key][1], d[key][2])
#         elif y == 5:
#             b = int(input('введите его количество для покупки в граммах:'))
#             while b > d[key][2]:
#                 print('на складе недостаточное количество товара, max для заказа: ', d[key][2])
#                 b = int(input('введите его количество, доступное для заказа:'))
#             print("ваша цена: ", b * d[key][1] / 100)
#             print("на складе осталось данных позиций: ", d[key][1] - b)
#         elif y == 6:
#             print('до свидания!')

    # b = int(input('введите его количество для покупки:'))
    # while b > d[key][2]:
    #     print('на складе недостаточное количество товара, max для заказа: ', d[key][2])
    #     b = int(input('введите его количество, доступное для заказа:'))
    # print("ваша цена: ", b * d[key][1]/100)
    # print("на складе осталось данных позиций: ", d[key][1] - b)
    # vibor = input("введите 'yes', если хотите продолжить покупки: ")


# x = open('abc.txt', 'r')
# a = x.readlines()
# print(a)
# b = []
# for i in range(len(a)):
#     a[i] = a[i].replace('\n', '')
# for i in a:
#     b.append(i.split(':'))
# print(b)
# d = dict(b)
# d1 = {}
# print(d)
# spis = []
# for key in d:
#     spis.append(d[key])
#     print(d.sort())
# x.close()


