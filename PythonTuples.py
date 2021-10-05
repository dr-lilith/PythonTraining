my_tuple = tuple(input("input the phrase:").split(" "))
counter = 0
for i in my_tuple:
    if i == "python" or i == "кортеж":
        counter += 1
print(counter)

A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
sum_1 = sum(A)
sum_2 = sum(B)
if sum_2 > sum_1:
    print("сумма больше в кортеже - ", "B")
if sum_1 > sum_2:
    print("сумма больше в кортеже - ", "A")

s = min(A)
print(s)

min = 10000
number = -1
for i in A:
    if i < min:
        index = number + 1
        min = i
    number += 1
print(index)

min2 = 10000
number2 = -1
for l in B:
    if l < min2:
        index2 = number2 + 1
        min2 = l
    number2 += 1
print(index2)


m = 1
for i in A:
    m *= i
print(m)

n = 1
for l in B:
    n *= l
print(n)


