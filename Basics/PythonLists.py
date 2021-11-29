# a = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in a:
#     if i <= 5:
#         print(i)
#
#

# a = []
# i = 0
# while i < 17:
#     a.append(0)
#     if i == 0 or i == 16:
#         a[i] = 1
#     i += 1
# print(a)


# lst = []
# i = 0
# while i < 5:
#     lst.append(int(input("input the number of the list:")))
#     i += 1
# print(lst)
# max_num = lst[0]
# for l in lst:
#     if l > max_num:
#         max_num = l
# print(max_num)


# a = []
# i = 1
# while i < 25:
#     if i % 2 == 0:
#         a.append(i)
#     i += 1
# print(a)
#
# s = 0
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16]
# s = sum(a)
# print(s)

# s = 1
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16]
# for i in a:
#     s = s * i
# print(s)


# a = [2, 3, 4, 5, 6, 7, 8, 9, -10, 11, 12, 1, 13, 14, 15, 16]
# s = a[0]
# for i in a:
#     if i < s:
#         s = i
# print(s)


# a = [2, 3, 4, 5, 6, 7, 8, 9, -10, 11, 12, 1, 13, 14, 15, 16]
# s = min(a)
# print(s)
#
# a = [2, 3, 4, 5, 6, 7, 8, 9, -10, 11, 12, 1, 13, 14, 15, 16]
# s = max(a)
# print(s)


# list1 = [15,48,'hello',6,19,'world']
# # все числа проверить на четность. если четное - то посчитать сумму его цифр. Еслинечетное - то заменить его на 1 в списке
# # все слова: посчитать количество гласных и согласных
# a = []
# for i in list1:
#     if i is int:
#         print(i)
#         for t in str(i):
#             a.append(t)
# print(a)

# a = [1,2,3,4,5]
# b = ['one', 'two', 'three', 'four', 'five']
# d = dict(zip(a, b))
# print(d)

d = dict(zip(['apple', 'candy', 'tomato', 'juice', 'ice cream', 'tea'],[[1,30], [2,25], [1,23], [2,24], [3,20], [4,15]]))
print(d)
print("наличие на складе:")
for key in d:
     print(key, " - цена: ", d[key][0], ' - количество на складе: ', d[key][1])
a = input('введите нужный Вам товар:')
while a not in d:
     print('такой товар не найден')
     a = input('введите нужный Вам товар из имеющихся на складе:')
b = int(input('введите его количество:'))
while b > d[a][1]:
     print('на складе недостаточное количество товара, max для заказа: ', d[a][1])
     b = int(input('введите его количество, доступное для заказа:'))
print("ваша цена: ", b * d[a][0])
print("на складе осталось данных позиций: ", d[a][1] - b)


