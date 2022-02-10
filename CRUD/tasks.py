import datetime
import uuid

tasks_list = []
task_object_list = []
task_id: int = 0


class Task:
    def __init__(self, title, description, time_of_creation, status, reporter, assignee) -> None:
        self.title = title
        self.description = description
        self.time_of_creation = time_of_creation
        global task_id
        self.id = uuid.uuid4()
        task_id += 1
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
    global task_id
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
    return Task(title, description, time_of_creation, status, reporter, assignee)


def overwriting_tasks_information() -> None:
    with open('saved_tasks.txt', "w") as saved:
        for task in task_object_list:
            for item in [task.title, task.description, task.time_of_creation, task.status, task.reporter,
                         task.assignee]:
                saved.write("%s " % item)
            saved.write('\n')
