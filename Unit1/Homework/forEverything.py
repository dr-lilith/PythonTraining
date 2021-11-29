network = input(
    'Введите номер сети и маску подсети в формате x.x.x.x/y, где x.x.x.x - IP адрес, а у - префикс маски подсети:  ')
a = network.split('/')
ip_list = a[0].split('.')
ip_list1 = ip_list.copy()
mask = int(a[1])
n = mask // 8
ost = mask % 8
# b1 = bin(int(b[0]))
# b2 = bin(int(b[1]))
# b3 = bin(int(b[2]))
# b4 = bin(int(b[3]))
# print(b1, b2, b3, b4)

# 194.20.140.151/30
masklist = ['128', '192', '224', '240', '248', '252', '254']
for i in range(1, 8):
    if i == ost:
        ip_list1[n] = masklist[i - 1]
for i in range(4):
    if i < n:
        ip_list1[i] = '255'
for i in range(4):
    if i > n:
        ip_list1[i] = '0'
newmask = ".".join(ip_list1)
print('Маска подсети: ', newmask)
ip_list2 = ip_list.copy()
step = 2 ** ((32 - mask) % 8)
for i in range(int(ip_list2[n]), 0, -1):
    if i % step == 0:
        ip_part = i
        break
for i in range(4):
    if i > n:
        ip_list2[i] = '0'
ip_list2[n] = str(ip_part)
network_ip_adress = ".".join(ip_list2)
print("IP адрес сети: ", network_ip_adress)

hosts = 2 ** (32 - mask)
available_hosts = hosts - 2
print("Количество доступных адресов в порции хоста: ", hosts)
print("Количество рабочих адресов для хостов ((2^n)-2): ", available_hosts)
