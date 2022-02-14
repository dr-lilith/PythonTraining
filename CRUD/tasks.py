import datetime
import uuid
import enum

tasks_list = []
task_object_list = []


class Task:
    def __init__(self, title: str, description: str, time_of_creation: datetime, status: str, reporter: str,
                 assignee: str) -> None:
        self.title = title
        self.description = description
        self.time_of_creation = time_of_creation
        self.id = uuid.uuid4()
        self.reporter = reporter
        self.status = status
        self.assignee = assignee
        task_object_list.append(self)
        tasks_list.append(self.id)
        with open('saved_tasks.txt', mode="a") as saved_tasks:
            for item in [self.title, self.description, self.time_of_creation, self.status, self.reporter,
                         self.assignee]:
                saved_tasks.write(f'{item} ')
            saved_tasks.write('\n')

    def __repr__(self) -> str:
        return self.title


def create_task() -> Task:
    title = get_field('title')
    description = get_field('description')
    time_of_creation = datetime.datetime.utcnow()
    status = TaskStatus.created.value
    reporter = get_field('reporter')
    assignee = get_field('assignee')
    return Task(title, description, time_of_creation, status, reporter, assignee)


def get_field(field_name) -> str:
    field = None
    while not field:
        field = input('Input the {} '.format(field_name))
        for i in field:
            if i == ' ':
                field = field.replace(i, '')
    return field


class TaskStatus(enum.Enum):
    created = 'created'
    accepted = 'accepted'
    inprogress = 'inprogress'
    completed = 'completed'


def overwrite_tasks_information() -> None:
    with open('saved_tasks.txt', "w") as saved:
        for task in task_object_list:
            for item in [task.title, task.description, task.time_of_creation, task.status, task.reporter,
                         task.assignee]:
                saved.write("%s " % item)
            saved.write('\n')
