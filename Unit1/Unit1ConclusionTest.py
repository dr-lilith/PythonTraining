# TASK 1
# 1. С клавиатуры вводится 7 значное число. Если четных цифр в нем больше, чем
# нечетных, то найти сумму всех его цифр, если нечетных больше, то найти
# произведение 1 3 и 6 цифры.

print('TASK 1: ')
your_number = int(input("Введите 7 значное число: "))
while your_number >= 10000000 or your_number <= 999999:
    print("Вы ввели не 7 значное число. Попробуйте еще раз. ")
    your_number = int(input("Введите 7 значное число: "))
digits = []
for i in str(your_number):
    digits.append(int(i))
print(digits)
odd = []
even = []
for i in digits:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
if len(even) < len(odd):
    print(digits[0] * digits[2] * digits[5])
elif len(even) > len(odd):
    print(sum(digits))
else:
    print("Количество четных и нечетных цифр равно")

# TASK 2
# С клавиатуры вводится текст с пробелами, но без знаков препинания. Определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.

print('TASK 2: ')
text = input("введите буквенный текст: ")
text = text.replace(' ', '')
vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю', 'Ё']
vowelsInText = []
for l in text:
    for i in vowels:
        if l == i:
            vowelsInText.append(i)
consonantsInText = len(text) - len(vowelsInText)
print("Гласных: ", len(vowelsInText), "   Cогласных: ", consonantsInText)
if len(vowelsInText) == consonantsInText:
    print(vowelsInText)

# TASK 3
# Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
# Посчитать, сколько раз сумма чисел, введенных с клавиатуры окажется больше
# суммы рандомной пары чисел. Проверку выполнить 7 раз.
# Если введенная пара окажется больше случайной в большинстве случаев из 7, то вывести случайные числа, сгенерированные в 4 итерации.

print('TASK 3: ')
import random

attempt = 1
win = 0
while attempt < 8:
    first = int(input('Введите первое число от 1 до 20'))
    second = int(input('Введите второе число от 1 до 20'))
    firstComp = random.randint(1, 20)
    secondComp = random.randint(1, 20)
    if first + second > firstComp + secondComp:
        win += 1
    if attempt == 4:
        a = firstComp
        b = secondComp
    attempt += 1
print("Введенная пара чисел оказалась больше рандомно сгенерированной ", win, " раз из 7 попыток")
if win >= 4:
    print(a, b)

# TASK 4
# Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно

print('TASK 4: ')
import random

amount = int(input("Введите количество случайных чисел:"))
digit = int(input("Введите искомую цифру в них: "))
attempt = 1
count = 0
while attempt <= amount:
    number = random.randint(1, 999)
    numberList = []
    for i in str(number):
        numberList.append(int(i))
    for l in numberList:
        if l == digit:
            count += 1
    attempt += 1
print("Введенная цифра встретилась {} раз".format(count))

# TASK 5
# Вводится строка, содержащая буквы, целые неотрицательные цифры и иные символы.
# Требуется все цифры, которые встречаются в строке отдельно вывести на экран. Строка
# может содержать пробелы

print('TASK 5: ')
text = input("Вводите строку, содержащую буквы, целые неотрицательные цифры и иные символы:")
numbers = []
for i in text:
    if i.isdigit():
        numbers.append(i)
print(numbers)

# TASK 6
# Даны два списка, состоящих из чисел и строк. Выведите список чисел из обоих списков, отсортированный по убыванию,
# а также, длину этого списка.

print('TASK 6: ')
a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 'test', 3]
c = a + b
d = []
for i in c:
    if type(i) == int:
        d.append(i)
print(d)
print("длинна списка = {0} элементов".format(len(d)))
d.sort(reverse=True)
print(d)

# TASK 7
# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
# веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
# также сколько всего букв в слове, сколько гласных и согласных

print('TASK 7: ')
word = input("введите слово: ")
pair = 0
k = 0
while k < (len(word) - 1):
    if word[k].islower() and word[k + 1].islower() or word[k].isupper() and word[k + 1].isupper():
        pair += 1
        k += 1
    k += 1
vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё', 'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю', 'Ё']
vowelsInText = []
for l in word:
    for i in vowels:
        if l == i:
            vowelsInText.append(i)
consonantsInText = len(word) - len(vowelsInText)
print(
    "Гласных: {}; Согласных : {}, Длина слова: {}, Пар одного регистра: {}".format(len(vowelsInText), consonantsInText,
                                                                                   len(word), pair))

# TASK 8
# Расположить числа от 10 до 21 и наоборот таким образом:
# 10 11 12 13                      21 20 19 18
# 14 15 16 17           и          17 16 15 14
# 18 19 20 21                      13 12 11 10
# Вывести на экран суммы всех строк и столбцов.
print('TASK 8: ')
numberList = [[10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21]]
print(numberList, type(numberList))
for i in range(3):
    for j in range(4):
        print(numberList[i][j], end=" ")
    print()
print("row sums:")
for i in range(3):
    s = 0
    for j in range(4):
        s = s + numberList[i][j]
    print(s)

print("column sums:")
for i in range(4):
    s = 0
    for j in range(3):
        s = s + numberList[j][i]
    print(s)

print('pause')
for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(numberList[i][j], end=" ")
    print()
print("row sums:")
for i in range(2, -1, -1):
    s = 0
    for j in range(3, -1, -1):
        s = s + numberList[i][j]
    print(s)
print("column sums:")
for i in range(3, -1, -1):
    s = 0
    for j in range(2, -1, -1):
        s = s + numberList[j][i]
    print(s)

# TASK 9
# Вывести на экран все совершенные числа от 1 до 10000.
# Соверше́нное число́ — натуральное число, равное сумме всех своих собственных делителей
# (то есть всех положительных делителей, отличных от самого́ числа). Например, число 6 равно сумме своих собственных
# делителей 1 + 2 + 3.

print('TASK 9: ')
for i in range(2, 10000):
    f = 0
    for j in range(1, int(i // 2) + 1):
        if i % j == 0:
            f += j
    if f == i:
        print(i)

# TASK 10
# Создайте словарь, связав его с переменной school, и наполните данными, которые бы отражали количество учащихся в разных
# классах (1а, 1б, 2б, 6а, 7в и т. п.). Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован (удален) другой класс. Вычислите
# общее количество учащихся в школе. Отсортируйте классы по возрастанию. Выведите в формате класс - количество учащихся

print('TASK 10: ')
school = dict(zip(['1a', '1b', '2b', '5a', '6b', '7a'], [12, 19, 25, 24, 26, 20]))
print(school)
school['1a'] = 10
print(school)
school['4a'] = 16
print(school)
school.pop('1a')
print(school)
total = 0
for i in school:
    total += school[i]
print(total)
numbers = []
schoolSort = {}
for i in school:
    numbers.append(school[i])
print(numbers)
numbers.sort()
print(numbers)
for i in numbers:
    for key in school:
        if school[key] == i:
            schoolSort[key] = i
print(schoolSort)
