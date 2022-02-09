import os
from users import User, create_user, login, check_credentials, account, user_account, admin_account, admin_tasks, \
    after_admin_editing, change_user_information, personal_tasks, work_on_task, overwriting_users_information, \
    overwriting_tasks_information, welcome
from tasks import Task, create_task, tasks_list, task_object_list, task_id


def creating_from_file(filename: str, classname) -> None:
    if os.path.exists(filename):
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
    create_task()
    welcome()

# TASK1 kuhyjmbgtf 22.01.22 completed Ivan Irina
# TASK2 jhmnhgbfvd 24.01.22 completed Ivan Alex
# TASK3 jmnhbgf 25.01.22 completed Andrew Ivan
# TASK4 mjhbgfvd 27.01.22 inprogress Andrew Irina
# TASK5 jkyujtrhbfrvdc 28.01.22 inprogress Alex Irina
# TASK6 k,jhmuyhngbftrfvdcs 29.01.22 inprogress Ivan Irina
# TASK7 mjyunhtrgvcew 01.02.22 created Ivan Irina


# Ivan 111 iTechArt ivan@gmail.com Softwareengineer 06.09.20 2
# Alex 111 iTechArt alex@gmail.com Dataengineer 25.07.21 2
# Irina 1111 iTechArt irina@gmail.com trainee 20.01.22 1
# Andrew 111 iTechArt andrew@gmail.com Dataengineer 21.01.22 2
