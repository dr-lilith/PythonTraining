import sys
import datetime

# from users import users
# from tasks import tasks
# from CRUD import tasks

user_id = 0
users_list = []
user_object_list = []
task_id = 0
tasks_list = []
task_object_list = []


def welcome():
    print('WELCOME TO MY LITTLE TRAINEE \'JIRA\' :)\n', '*' * 40)
    command = input(('Log in to use the program\n[C]reate user\n[L]ogin')).upper()
    while command != 'C' and command != 'L':
        command = input('Input the right command: C - create or L - login')
        command = command.upper()
    if command == 'C':
        create_user()
        print(users_list)
    elif command == 'L':
        login()


class User:

    def __init__(self, name, password, company, email, position, time_of_creation, urole):
        self.name = name
        self.password = password
        self.company = company
        self.email = email
        self.position = position
        self.time_of_creation = time_of_creation
        self.role = urole
        global user_id
        self.id = user_id
        user_id += 1
        user_object_list.append(self)
        users_list.append(name)
        with open('saved_users.txt', mode="a") as saved_users:
            for item in [self.name, self.password, self.company, self.email, self.position, self.time_of_creation,
                         str(self.role)]:
                saved_users.write("%s " % item)
            saved_users.write('\n')

    def __repr__(self):
        return f"{self.name}"

    def create_task(self):
        global task_id
        task_object = 'task' + str(task_id)
        task_id += 1
        tasks_list.append(task_object)
        title = input('Input the title of the task: ')
        description = input('Input the description of the task: ')
        reporter = input('Input the reporter of the task: ')
        assignee = input('Input the assignee of the task: ')
        task_object = Task(title, description, reporter, assignee)
        return task_object


def create_user():
    def _get_user_field(field_name):
        field = None

        while not field:
            field = input('Input the USER {} '.format(field_name))
            for i in field:
                if i == ' ':
                    field = field.replace(i, '')
        return field

    def _get_user_password():
        user_password = None
        while not user_password:
            user_password = input('What is the user password?')
            user_password2 = input('Repeat your password')
            if user_password != user_password2:
                print('Passwords mismatch. Try again')
                user_password = None

            if user_password == 'exit':
                user_password = None
                break

        if not user_password:
            sys.exit()

        return user_password

    name = _get_user_field('name')
    password = _get_user_password()
    company = _get_user_field('company')
    email = _get_user_field('email')
    position = _get_user_field('position')
    time_of_creation = datetime.datetime.utcnow()
    urole = None
    while not urole:
        urole = int(input('Input the role: 1 - user  2 - admin'))

    name = User(name, password, company, email, position, time_of_creation, urole)


def login():
    user_name = input('Input the USER name: ')
    while user_name not in users_list:
        user_name = input(
            'Sorry, this user doesn\'t exists. If you want to exit, just input exit instead of user name. Input the USER name: ')
        if user_name == 'exit':
            return welcome()
    user_password = input('Input the USER password: ')
    return check_credentials(user_name, user_password)


def check_credentials(user_name, user_password):
    for user in user_object_list:
        if user.name == user_name and user.password == user_password:
            print(f'You\'ve successfully logged in! Welcome, {user.name} :)')
            return user_account(user)
        while user.name == user_name and user.password != user_password:
            user_password = input(
                'Sorry, this password is wrong. If you want to exit, just input exit instead of user password. Input the USER password: ')
            if user.name == user_name and user.password == user_password:
                print(f'You\'ve successfully logged in! Welcome, {user.name} :)')
                return user_account(user)
            if user_password == 'exit':
                return welcome()


def user_account(user: User):
    with open('saved_tasks.txt') as saved_tasks:
        saved_tasks_from_file = saved_tasks.readlines()
    saved_tasks_from_file = list(map(lambda s: s.strip(), saved_tasks_from_file))
    task_for_user = 0
    task_by_user = 0
    count = -1
    tasks_for_user = []
    tasks_by_user = []
    for task in saved_tasks_from_file:
        count += 1
        task = task.split(' ')
        if task[-1] == user.name:
            task_for_user += 1
            tasks_for_user.append(task_object_list[count])
            # edit create view
        if task[-2] == user.name:
            task_by_user += 1
            tasks_by_user.append(task_object_list[count])
    print(f'{user.name}, you have {task_for_user} task(s): ')
    for task in tasks_for_user:
        print(task)
    menu = input(f'THE MAIN MENU. CHOOSE OPERATION: \n   -   [W]ork on a task\n   -   [C]hange USER information\n'
                 f'   -   [L]og out\n   -   [D]elete account (delete this user)\nInput 1 letter (w/c/l/d): ').upper()
    if menu == 'W':
        work_on_task(tasks_for_user, user)
    if menu == 'C':
        change_user_information(user)
        overwriting_users_information()
        user_account(user)
    if menu == 'L':
        return welcome()
    if menu == 'D':
        user_object_list.remove(user)
        del user
        overwriting_users_information()


def change_user_information(user):
    print(f'Current user information: \n[N]ame   -   {user.name}\n[PA]ssword   -   ', len(user.password) * '*',
          f'\n[C]ompany   -   {user.company}\n[E]mail   -   {user.email}\n[PO]sition   -   {user.position}'
          f'\n[R]ole   -   {user.role}\nTime of creation   -   {user.time_of_creation} (immutable parameter)')
    choice = input('Input first letter(s) of parameter you want to change ( n / pa / c / e / po / r )').upper()
    if choice == 'N':
        name = input('Input the new USER name: ')
        user.name = name
    if choice == 'PA':
        old_password = user_password = ''
        user_password2 = ' '
        while old_password != user.password:
            old_password = input('In order to change password, input your PASSWORD or exit to return: ')
            if old_password == 'exit':
                return user_account(user)
            while user_password != user_password2:
                user_password = input('Input your new password: ')
                user_password2 = input('Repeat your new password: ')
                if user_password != user_password2:
                    print('Passwords mismatch. Try again.')
            user.password = user_password
            overwriting_users_information()
            user_account(user)
    if choice == 'C':
        company = input('Input the new USER company: ')
        user.company = company
    if choice == 'E':
        email = input('Input the new USER email: ')
        user.email = email
    if choice == 'PO':
        position = input('Input the new USER position: ')
        user.position = position
    if choice == 'R':
        role = ''
        while role != '1' and role != '2':
            role = input('Input the new USER role: 1 - user or 2 - admin')
            user.role = role


def work_on_task(tasks_for_user, user):
    choice = None
    while choice == None:
        try:
            choice = int(input('Input the number of the task you would like to work on (starting from 0) :'))
        except ValueError:
            choice = int(
                input('Invalid input! Input the number of the task you would like to work on (starting from 0) :'))
    choice1 = ''
    while choice1 != 'y' and choice1 != 'n':
        choice1 = input(f'Title: {tasks_for_user[choice].title} \nDescription: {tasks_for_user[choice].description} \n'
                        f'Task status: {tasks_for_user[choice].status} \nCreation_time : '
                        f'{tasks_for_user[choice].time_of_creation} \nReporter: {tasks_for_user[choice].reporter} \n'
                        f'Do you want to change the status of this task? (input Y to change the status or N to return '
                        f'back): ')
    choice1 = choice1.upper()
    if choice1 == 'Y':
        tasks_for_user[choice].status = input('Input the new status (created, accepted, inprogress or completed): ')
        overwriting_tasks_information()
        print(f'INFORMATION UPDATED.\nTitle: {tasks_for_user[choice].title} \nDescription: '
              f'{tasks_for_user[choice].description} \nTask status: {tasks_for_user[choice].status} \nCreation_time : '
              f'{tasks_for_user[choice].time_of_creation} \nReporter: {tasks_for_user[choice].reporter}')
        user_account(user)
    if choice1 == 'N':
        user_account(user)
    # if user.role == 2:
    #     print(f'{user.name}, you have created {task_by_user} task(s): ')
    #     for task in tasks_by_user:
    #         print(task)


# user_object_list.append(self)
#         users_list.append(name)
#         with open('saved_users.txt', mode="a") as saved_users:
#             for item in [self.name, self.password, self.company, self.email, self.position, self.time_of_creation,
#                          str(self.role)]:
#                 saved_users.write("%s " % item)
#             saved_users.write('\n')


def overwriting_users_information():
    with open('saved_users.txt', "w") as saved:
        for user in user_object_list:
            for item in [user.name, user.password, user.company, user.email, user.position, user.time_of_creation,
                         str(user.role)]:
                saved.write("%s " % item)
            saved.write('\n')
    print('Information successfully updated.')


def overwriting_tasks_information():
    with open('saved_tasks.txt', "w") as saved:
        for task in task_object_list:
            for item in [task.title, task.description, task.time_of_creation, task.status, task.reporter,
                         task.assignee]:
                saved.write("%s " % item)
            saved.write('\n')


class Task:
    def __init__(self, title, description, time_of_creation, status, reporter, assignee):
        self.title = title
        self.description = description
        self.time_of_creation = time_of_creation
        global task_id
        self.id = task_id
        task_id += 1
        self.reporter = reporter
        self.status = status
        self.assignee = assignee
        task_object_list.append(self)
        tasks_list.append(self.id)
        with open('saved_tasks.txt', mode="a") as saved_tasks:
            for item in [self.title, self.description, self.time_of_creation, self.status, self.reporter,
                         self.assignee]:
                saved_tasks.write("%s " % item)
        with open('saved_tasks.txt', mode="a") as saved_tasks:
            saved_tasks.write('\n')

    def __repr__(self):
        return f"{self.title}"


def create_task():
    global task_id
    task_object = 'task' + str(task_id)
    task_id += 1

    def _get_task_field(field_name):
        field = None
        while not field:
            field = input('Input the TASK {} '.format(field_name))
            for i in field:
                if i == ' ':
                    field = field.replace(i, '')
        return field

    title = _get_task_field('title')
    description = _get_task_field('description')
    time_of_creation = datetime.datetime.utcnow()
    status = 'created'
    reporter = _get_task_field('reporter')
    assignee = _get_task_field('assignee')
    task_object = Task(title, description, time_of_creation, status, reporter, assignee)
    return task_object


class Repository:
    def init(self, list: list):
        self._list = list

    def add(self, entity):
        self._list.append(entity)

    def save(self):
        pass

    def load(self):
        pass

    def search(self, filter) -> Task:
        pass


def creating_from_file(filename: str, classname):
    with open(filename) as saved:
        saved_from_file = saved.readlines()
    saved_from_file = list(map(lambda s: s.strip(), saved_from_file))
    open(filename, "w").close()
    for string in saved_from_file:
        args = string.split()
        args[0] = classname(*args)


if __name__ == '__main__':
    creating_from_file('saved_tasks.txt', Task)
    creating_from_file('saved_users.txt', User)
    # create_task()
    # create_user()
    welcome()

# TASK1 kuhyjmbgtf 22.01.22 completed Ivan Irina
# TASK2 jhmnhgbfvd 24.01.22 completed Ivan Alex
# TASK3 jmnhbgf 25.01.22 completed Andrew Ivan
# TASK4 mjhbgfvd 27.01.22 inprogress Andrew Irina
# TASK5 jkyujtrhbfrvdc 28.01.22 inprogress Alex Irina
# TASK6 k,jhmuyhngbftrfvdcs 29.01.22 inprogress Ivan Irina
# TASK7 mjyunhtrgvcew 01.02.22 created Ivan Irina
#
#
#
#
# Ivan 111 iTechArt ivan@gmail.com Softwareengineer 06.09.20 2
# Alex 111 iTechArt alex@gmail.com Dataengineer 25.07.21 2
# Irina 1111 iTechArt irina@gmail.com trainee 20.01.22 1
# Andrew 111 iTechArt andrew@gmail.com Dataengineer 21.01.22 2
