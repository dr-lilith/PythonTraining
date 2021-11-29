#    ПРАКТИЧЕСКИЕ ЗАДАЧИ


#        №1

# 1.	По двум введенным пользователем катетам вычислить длину гипотенузы.

a = int(input("Введите длину первого катета"))
b = int(input("Введите длину второго катета"))
c = (a ** 2 + b ** 2) ** 0.5
print("Длинна гипотенузы = ", c)

#         № 2

# 2.	Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

number1 = int(input("input the first number:"))
number2 = int(input("input the second number:"))
number3 = int(input("input the third number:"))
if number2 < number1 < number3 or number3 < number1 < number2:
    print(number1)
if number1 < number2 < number3 or number3 < number2 < number1:
    print(number2)
if number2 < number3 < number1 or number1 < number3 < number2:
    print(number3)

#         № 3

# 3.	Из двух случайных чисел, одно из которых четное, а другое нечетное, определить и вывести на экран нечетное число.

number1 = int(input("input the first number(odd):"))
number2 = int(input("input the second number(even):"))
if number1 % 2 == 0:
    print("the second number is odd: ", number2)
else:
    print("the first number is odd: ", number1)


#       № 4

# 4.	Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, то надо вывести число 6843.

#
number = int(input("input a 4 digit number:"))
string = str(number)
print(string[::-1])

#            ТАБЛИЦА УМНОЖЕНИЯ

for i in range(2, 10):
    for k in range(1, 10):
        print(i, "*", k, "= ", i * k, ";  ", end="")
print()
print()

#      № 5

# 5.	Вывести на экран “прямоугольник”, образованный из двух видов символов. Контур прямоугольника должен состоять
# из одного символа, а в “заливка” – из другого.

y = int(input("введите длинную сторону прямоугольника:"))
x = int(input("введите короткую сторону прямоугольника:"))
for i in range(x):
    if i == 0 or i == x - 1:
        for p in range(y):
            print("@", end="")
    else:
        for j in range(y):
            if j == 0 or j == y - 1:
                print("@", end="")
            else:
                print("*", end="")
    print()

#       № 6
# 6.	Найти все совершенные числа до 10000. Совершенное число – это такое число, которое равно сумме всех своих
# делителей, кроме себя самого.
# Например, число 6 является совершенным, т.к. кроме себя самого делится на числа 1, 2 и 3, которые в сумме дают 6.

a = []
for i in range(3, 10001):
    for k in range(1, i // 2 + 1):
        if i % k == 0:
            a.append(k)
    if i == sum(a):
        print(i)
    a = []

#       № 7

# 7.	Заполнить вводом с клавиатуры численный массив за исключением последнего элемента, вывести его на экран.
# Запросить еще одно значение и его позицию в массиве. Вставить указанное число в заданную позицию, подвинув элементы
# после него.

a = []
b = int(input("какое количество чисел будет в массиве?:"))
for i in range(b + 1):
    if i == b:
        last = int(input("Введите элемент массива:"))
        print(last, " - это последний элемент, превышающее заданное количество чисел в массиве, в массив не включается")
    elif i < b:
        a.append(int(input("Введите элемент массива:")))
print(a)
new = int(input("Введите новый элемент массива:"))
place = int(input("Введите позицию нового элемента массива:"))
a.insert(place, new)
print(a)

#         № 8


# 8.	Вводится строка, состоящая из слов, разделенных пробелами. Требуется посчитать количество слов в ней.

a = input("Введите строку из слов, разделенных пробелами:")
b = a.split(" ")
print(len(b), "слов(а) в строке")

#           № 9

# 9.	Введите строку c клавиатуры, которая состоит из букв разных регистров. Нужно очистить эту строку от всех
# заглавных букв и вывести результат на экран.
string = input("Введите строку, которая состоит из букв разных регистров:")
our_list = []
for i in string:
    if not i.isupper():
        our_list.append(i)
print("".join(our_list))

#           № 10

# 10.	Найти совпадающие элементы двух списков.
# a = [5,[1,2],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
#        Эти значения записать в новый список

a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)
