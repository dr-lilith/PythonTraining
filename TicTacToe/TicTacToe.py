print(
    "ЭТО ИГРА КРЕСТИКИ-НОЛИКИ. ПОБЕЖДАЕТ ТОТ, КТО ПЕРВЫМ УСПЕЛ ЗАНЯТЬ ПОЛНОСТЬЮ ДИАГОНАЛЬ ИЛИ ЛИНИЮ.\nВыбор делается,"
    " как в морском бою(например, a1 или с3)")
c = [['      1 ', ' 2 ', ' 3 '], [' a ', " * ", ' * ', ' * '], [' b ', " * ", ' * ', ' * '],
     [' c ', " * ", ' * ', ' * ']]


def game():
    print(str(c[0][0]), str(c[0][1]), str(c[0][2]), '\n', str(c[1][0]), str(c[1][1]), str(c[1][2]),
          str(c[1][3]), '\n', str(c[2][0]), str(c[2][1]), str(c[2][2]), str(c[2][3]), '\n', str(c[3][0]), str(c[3][1]),
          str(c[3][2]), str(c[3][3]))


def first():
    if hod1[0] == "a":
        if hod1[1] == '1':
            c[1][1] = ' + '
        elif hod1[1] == '2':
            c[1][2] = ' + '
        elif hod1[1] == '3':
            c[1][3] = ' + '
    elif hod1[0] == "b":
        if hod1[1] == '1':
            c[2][1] = ' + '
        elif hod1[1] == '2':
            c[2][2] = ' + '
        elif hod1[1] == '3':
            c[2][3] = ' + '
    elif hod1[0] == "c":
        if hod1[1] == '1':
            c[3][1] = ' + '
        elif hod1[1] == '2':
            c[3][2] = ' + '
        elif hod1[1] == '3':
            c[3][3] = ' + '


def second():
    if hod2[0] == "a":
        if hod2[1] == '1':
            c[1][1] = ' o '
        elif hod2[1] == '2':
            c[1][2] = ' o '
        elif hod2[1] == '3':
            c[1][3] = ' o '
    elif hod2[0] == "b":
        if hod2[1] == '1':
            c[2][1] = ' o '
        elif hod2[1] == '2':
            c[2][2] = ' o '
        elif hod2[1] == '3':
            c[2][3] = ' o '
    elif hod2[0] == "c":
        if hod2[1] == '1':
            c[3][1] = ' o '
        elif hod2[1] == '2':
            c[3][2] = ' o '
        elif hod2[1] == '3':
            c[3][3] = ' o '


def check_victory():
    if c[1][1] == c[1][2] == c[1][3] != " * " or c[2][1] == c[2][2] == c[2][3] != " * " or c[3][1] == c[3][2] == \
            c[3][3] != " * " or c[1][1] == c[2][1] == c[3][1] != " * " or c[1][2] == c[2][2] == c[3][2] != " * " or \
            c[1][3] == c[2][3] == c[3][3] != " * " or c[1][1] == c[2][2] == c[3][3] != " * " or c[1][3] == c[2][
        2] == c[3][1] != " * ":
        print("ПОБЕДА!")
        return True


game()

while True:
    hod1 = input("Игрок номер 1, вы играете крестиками 'x'. Ваш ход: ")
    first()
    game()
    if check_victory():
        break
    hod2 = input("Игрок номер 2, вы играете ноликами 'o'. Ваш ход: ")
    second()
    game()
    if check_victory():
        break
