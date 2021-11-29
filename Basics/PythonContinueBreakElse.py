# s = ""
# for i in "hello world":
#     if i == "o":
#         continue
#     s += i
# print(s)


#
s = ""
# for i in "hello world":
#     if i == "r":
#         break
#     s += i
# print(s)

#
# s = ""
# for i in "hello world":
#     if i == "o":
#         continue
#     s += i
# print(s)

# MOI ZADACHI:

# i = 0
# while i <= 100:
#     if i%7 != 0:
#         print(i)
#         i += 1
#     else:
#         i += 1
#         continue


inpstr = input("Введите строку для проверки на наличие символа 'q'")
isq = False
for c in inpstr:
    if c == 'q':
        isq = True
        break

if isq == False:
    print("Программа успешно отработала, символ 'q' отсутствует")

