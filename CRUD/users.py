import datetime
import enum
import uuid
from tasks import task_object_list, tasks_list, overwrite_tasks_information, Task, create_task, TaskStatus, get_field

users_list = []
user_object_list = []


def welcome() -> None:
    print('WELCOME TO MY LITTLE TRAINEE \'JIRA\' :)\n', '*' * 40,
          '\nTo select, input the first letter of the selected command')
    command: str = input('Log in to use the program\n[C]reate user\n[L]ogin\n[V]iew common statistics\n').upper()
    while command not in [WelcomeInput.create_user.value, WelcomeInput.login.value, WelcomeInput.view_statistics.value]:
        command: str = input('Input the right command: C - create,  L - login or V - view common statistics').upper()
    if command == WelcomeInput.create_user.value:
        create_user()
        print(users_list)
    if command == WelcomeInput.login.value:
        login()
    if command == WelcomeInput.view_statistics.value:
        inprogrrss_count = 0
        for task in task_object_list:
            if task.status == TaskStatus.inprogress.value:
                inprogrrss_count += 1
        list_assignee = []
        dict_assignee = {}
        for task in task_object_list:
            if task.status == TaskStatus.completed.value:
                list_assignee.append(task.assignee)
        for user in user_object_list:
            dict_assignee[user.name] = list_assignee.count(user.name)
        try:
            leader = max(dict_assignee.values())
        except ValueError:
            leader = 'no top user'
        for key in dict_assignee:
            if dict_assignee[key] == leader:
                leader = key
        print('Number of users   -   ', len(user_object_list), '\nTotal number of tasks   -   ', len(task_object_list),
              '\nNumber of “in progress” tasks   -   ', inprogrrss_count,
              '\nTop user with the biggest number of completed tasks   -   ', leader)
        welcome()


class User:

    def __init__(self, name: str, password: str, company: str, email: str, position: str, time_of_creation: datetime,
                 urole: str) -> None:
        self.name = name
        self.password = password
        self.company = company
        self.email = email
        self.position = position
        self.time_of_creation = time_of_creation
        self.role = int(urole)
        self.id = uuid.uuid4()
        user_object_list.append(self)
        users_list.append(name)
        with open('saved_users.txt', mode="a") as saved_users:
            for item in [self.name, self.password, self.company, self.email, self.position, self.time_of_creation,
                         str(self.role)]:
                saved_users.write(f'{item} ')

            saved_users.write('\n')
        User.personal_tasks(self)

    def __repr__(self) -> str:
        return self.name

    def personal_tasks(self) -> None:
        my_tasks = []
        for task in task_object_list:
            if task.assignee == self.name:
                my_tasks.append(task)


def create_user() -> None:
    def _get_user_password() -> str:
        user_password = None
        while not user_password:
            user_password: str = input('What is the user password? ')
            user_password2: str = input('Repeat your password: ')
            if user_password != user_password2:
                print('Passwords mismatch. Try again ')
                user_password = None
            if user_password == 'exit':
                user_password = None
                break
        return user_password

    name = get_field('name')
    password = _get_user_password()
    company = get_field('company')
    email = get_field('email')
    position = get_field('position')
    time_of_creation = datetime.datetime.utcnow()
    urole = None
    while not urole:
        input_role = int(input('Input the role: 1 - user  2 - admin'))
        if input_role == Role.user.value:
            urole = Role.user.value
        if input_role == Role.admin.value:
            urole = Role.admin.value

    name = User(name, password, company, email, position, time_of_creation, str(urole))
    return welcome()


class Role(enum.Enum):
    user = 1
    admin = 2


class WelcomeInput(enum.Enum):
    create_user = 'C'
    login = 'L'
    view_statistics = 'V'


class AccountInput(enum.Enum):
    my_created_tasks = 'M'
    work = 'W'
    change = 'C'
    logout = 'L'
    delete = 'D'
    yes = 'Y'
    no = 'N'
    edit = 'E'
    view = 'V'
    title = 'T'
    description = 'D'
    status = 'S'
    assignee = 'A'


def login():
    user_name: str = input('Input the USER name: ')
    while user_name not in users_list:
        user_name: str = input(
            'Sorry, this user doesn\'t exists. If you want to exit, just input exit instead of user name. Input the '
            'USER name: ')
        if user_name == 'exit':
            return welcome()
    user_password: str = input('Input the USER password: ')
    return check_credentials(user_name, user_password)


def check_credentials(user_name, user_password) -> None:
    for user in user_object_list:
        if user.name == user_name and user.password == user_password:
            print(f'You\'ve successfully logged in! Welcome, {user.name} :)')
            return account(user)
        while user.name == user_name and user.password != user_password:
            user_password: str = input(
                'Sorry, this password is wrong. If you want to exit, just input exit instead of user password. Input '
                'the USER password: ')
            if user.name == user_name and user.password == user_password:
                print(f'You\'ve successfully logged in! Welcome, {user.name} :)')
                return account(user)
            if user_password == 'exit':
                return welcome()


def account(user: User):
    task_for_user = 0
    task_by_user = 0
    count = -1
    tasks_for_user = []
    tasks_by_user = []
    for task in task_object_list:
        count += 1
        if task.assignee == user.name:
            task_for_user += 1
            tasks_for_user.append(task_object_list[count])
        if user.role == Role.admin.value:
            if task.reporter == user.name:
                task_by_user += 1
                tasks_by_user.append(task_object_list[count])
    if user.role == Role.admin.value:
        print(f'{user.name}, you have created {task_by_user} task(s): ')
        for task in tasks_by_user:
            print(task)
    print(f'{user.name}, you have {task_for_user} task(s): ')
    for task in tasks_for_user:
        print(task)
    if user.role == Role.user.value:
        return user_account(user, tasks_for_user)
    if user.role == Role.admin.value:
        return admin_account(user, tasks_by_user, tasks_for_user)


def user_account(user: User, tasks_for_user) -> None:
    menu: str = input(f'THE MAIN MENU. CHOOSE OPERATION: \n   -   [W]ork on a task\n   -   [C]hange USER information\n'
                      f'   -   [L]og out\n   -   [D]elete account (delete this user)\nInput 1 letter (w/c/l/d): ').upper()
    if menu == AccountInput.work.value:
        work_on_task(tasks_for_user, user)
    if menu == AccountInput.change.value:
        change_user_information(user)
        overwrite_users_information()
        account(user)
    if menu == AccountInput.logout.value:
        return welcome()
    if menu == AccountInput.delete.value:
        user_object_list.remove(user)
        del user
        overwrite_users_information()


def admin_tasks(user: User, tasks_by_user, tasks_for_user) -> None:
    print(tasks_by_user)
    menu: str = input(' - [V]iew task\n - [E]dit task\n - [D]elete task\nInput the first letter:  ').upper()
    if menu == AccountInput.view.value:
        choice = None
        while choice == None:
            try:
                choice = int(input(
                    'Input the number of the task, information of which you would like to view (starting from 0) : '))
            except ValueError:
                choice = int(
                    input(
                        'Input the number of the task, information of which you would like to view(starting from 0): '))
        change: str = input(
            f' \n[T]itle: {tasks_by_user[choice].title} \n[D]escription: {tasks_by_user[choice].description}'
            f' \n[S]tatus: {tasks_by_user[choice].status} \n[A]ssignee: {tasks_by_user[choice].assignee} \n'
            f'Creation time : {tasks_by_user[choice].time_of_creation} (immutable parameter)\nInput the '
            f'first letter of the parameter you would like to change:  ').upper()
        if change == AccountInput.title.value:
            tasks_by_user[choice].title = input('Input the new title: ')
            after_admin_editing(user, tasks_by_user, tasks_for_user, choice)
        if change == AccountInput.description.value:
            tasks_by_user[choice].description = input('Input the new description: ')
            after_admin_editing(user, tasks_by_user, tasks_for_user, choice)
        if change == AccountInput.status.value:
            tasks_by_user[choice].status = input('Input the new status (created, accepted, inprogress or completed): ')
            after_admin_editing(user, tasks_by_user, tasks_for_user, choice)
        if change == AccountInput.assignee.value:
            tasks_by_user[choice].assignee = input('Input the new assignee: ')
            after_admin_editing(user, tasks_by_user, tasks_for_user, choice)
    if menu == AccountInput.delete.value:
        choice = None
        while not choice:
            try:
                choice = int(input('Input the number of the task you want to delete (starting from 0) : '))
            except ValueError:
                choice = int(
                    input('Input the number of the task you want to delete (starting from 0) : '))
        choice1: str = input(
            f'Title: {tasks_by_user[choice].title} \nDescription: {tasks_by_user[choice].description} \n'
            f'Task status: {tasks_by_user[choice].status} \nCreation_time : '
            f'{tasks_by_user[choice].time_of_creation} \nReporter: {tasks_by_user[choice].reporter} \n'
            f'Are you sure, you want to DELETE this task?'
            f' (input Y to DELETE or N to return back): ').upper()
        if choice1 == AccountInput.yes.value:
            for task in task_object_list:
                if task == tasks_by_user[choice]:
                    del task
            tasks_by_user.pop(choice)
            overwrite_tasks_information()
        if choice1 == AccountInput.no.value:
            return admin_account(user, tasks_by_user, tasks_for_user)
    if menu == AccountInput.edit.value:
        create_task()
        return admin_account(user, tasks_by_user, tasks_for_user)


def after_admin_editing(user, tasks_by_user, tasks_for_user, choice) -> None:
    overwrite_tasks_information()
    print(f'INFORMATION UPDATED.\nTitle: {tasks_by_user[choice].title} \nDescription: '
          f'{tasks_by_user[choice].description} \nTask status: {tasks_by_user[choice].status} \nReporter: '
          f'{tasks_by_user[choice].reporter} \nCreation time : {tasks_by_user[choice].time_of_creation}')
    admin_account(user, tasks_by_user, tasks_for_user)


def admin_account(user: User, tasks_by_user, tasks_for_user) -> None:
    menu: str = input(
        f'THE MAIN MENU. CHOOSE OPERATION: \n   -   [M]y created tasks\n   -   [W]ork on a task\n   -   [C]hange USER '
        f'information\n   -   [L]og out\n   -   [D]elete account (delete this user)\nInput 1 letter '
        f'(m/w/c/l/d): ').upper()
    if menu == AccountInput.my_created_tasks.value:
        admin_tasks(user, tasks_by_user, tasks_for_user)
    if menu == AccountInput.work.value:
        work_on_task(tasks_for_user, user)
    if menu == AccountInput.change.value:
        change_user_information(user)
        overwrite_users_information()
        account(user)
    if menu == AccountInput.logout.value:
        return welcome()
    if menu == AccountInput.delete.value:
        user_object_list.remove(user)
        del user
        overwrite_users_information()


class ChangeUserInfo(enum.Enum):
    name = 'N'
    password = 'PA'
    company = 'C'
    email = 'E'
    position = 'PO'
    role = 'R'


def change_user_information(user) -> None:
    print(f'Current user information: \n[N]ame   -   {user.name}\n[PA]ssword   -   ', len(user.password) * '*',
          f'\n[C]ompany   -   {user.company}\n[E]mail   -   {user.email}\n[PO]sition   -   {user.position}'
          f'\n[R]ole   -   {user.role}\nTime of creation   -   {user.time_of_creation} (immutable parameter)')
    choice: str = input('Input first letter(s) of parameter you want to change ( n / pa / c / e / po / r )').upper()
    if choice == ChangeUserInfo.name.value:
        name: str = input('Input the new USER name: ')
        user.name = name
    if choice == ChangeUserInfo.password.value:
        old_password = user_password = ''
        user_password2 = ' '
        while old_password != user.password:
            old_password: str = input('In order to change password, input your PASSWORD or exit to return: ')
            if old_password == 'exit':
                return account(user)
            while user_password != user_password2:
                user_password: str = input('Input your new password: ')
                user_password2: str = input('Repeat your new password: ')
                if user_password != user_password2:
                    print('Passwords mismatch. Try again.')
            user.password = user_password
            overwrite_users_information()
            account(user)
    if choice == ChangeUserInfo.company.value:
        company: str = input('Input the new USER company: ')
        user.company = company
    if choice == ChangeUserInfo.email.value:
        email: str = input('Input the new USER email: ')
        user.email = email
    if choice == ChangeUserInfo.position.value:
        position: str = input('Input the new USER position: ')
        user.position = position
    if choice == ChangeUserInfo.role.value:
        role = ''
        while role != Role.user.value and role != Role.admin.value:
            role = int(input('Input the new USER role: 1 - user or 2 - admin'))
            if role == Role.user.value or role == Role.admin.value:
                user.role = role


def work_on_task(tasks_for_user, user) -> None:
    choice = None
    while choice == None:
        try:
            choice = int(input('Input the number of the task you would like to work on (starting from 0) :'))
        except ValueError:
            choice = int(
                input('Invalid input! Input the number of the task you would like to work on (starting from 0) :'))
    choice1 = ''
    while choice1 != AccountInput.yes.value and choice1 != AccountInput.no.value:
        choice1: str = input(
            f'Title: {tasks_for_user[choice].title} \nDescription: {tasks_for_user[choice].description} \n'
            f'Task status: {tasks_for_user[choice].status} \nCreation_time : '
            f'{tasks_for_user[choice].time_of_creation} \nReporter: {tasks_for_user[choice].reporter} \n'
            f'Do you want to change the status of this task? (input Y to change the status or N to return '
            f'back): ').upper()
    if choice1 == AccountInput.yes.value:
        tasks_for_user[choice].status = input('Input the new status (created, accepted, inprogress or completed): ')
        overwrite_tasks_information()
        print(f'INFORMATION UPDATED.\nTitle: {tasks_for_user[choice].title} \nDescription: '
              f'{tasks_for_user[choice].description} \nTask status: {tasks_for_user[choice].status} \nCreation_time : '
              f'{tasks_for_user[choice].time_of_creation} \nReporter: {tasks_for_user[choice].reporter}')
        account(user)
    if choice1 == AccountInput.no.value:
        account(user)


def overwrite_users_information() -> None:
    with open('saved_users.txt', "w") as saved:
        for user in user_object_list:
            for item in [user.name, user.password, user.company, user.email, user.position, user.time_of_creation,
                         str(user.role)]:
                saved.write("%s " % item)
            saved.write('\n')
    print('Information successfully updated.')
