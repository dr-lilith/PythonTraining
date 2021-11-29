# a = 2
# b = 1
# while a <= 9435:
#     b *= a
#     a += 2
# print(b)

# c = 15
# while c <= 15 and c >= 1:
#     print(c)
#     c -= 1

a = int(input('input the first number'))
b = int(input('input the second number'))
if a > b:
    b += 1
    while b < 0:

        print(b)
        b += 1
elif b > a:
    a +=1
    while a < 0:

        print(a)
        a += 1

else:
    print('you input the same number twice')




