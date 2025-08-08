from datetime import datetime
import json

class Task:
    def __init__(self, status: str, description: str):
        self.status = status
        self.description = description
        self.createdAt = str(datetime.now())
        self.updatedAt = None


def add_task(status: str, description: str) -> int:
    id = None
    with open('tasks.json', 'r') as f:
        tasks = f.read()
        if tasks == '':
            id = 1
        else:
            tasks = json.loads(tasks)
            id = len(tasks)
            id += 1

    with open('tasks.json', 'w') as f:
        if id == 1:
            task = Task(status, description)
            task = {id: task.__dict__}
            json.dump(task, f, indent=2)
        else:
            task = Task(status, description)
            tasks[id] = task.__dict__
            json.dump(tasks, f, indent=2)

    return id


def mark_task_done(status: str, id: str) -> None:
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
        if id not in tasks.keys():
            raise KeyError
        tasks[id]['status'] = status
        tasks[id]['updatedAt'] = str(datetime.now())

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)


def mark_task_in_progress(status: str, id: str) -> None:
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
        if id not in tasks.keys():
            raise KeyError
        tasks[id]['status'] = status
        tasks[id]['updatedAt'] = str(datetime.now())

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)


def update_task(description: str, id: str) -> None:
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
        if id not in tasks.keys():
            raise KeyError
        tasks[id]['description'] = description
        tasks[id]['updatedAt'] = str(datetime.now())

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)


def delete_task(id: str) -> None:
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
        if id not in tasks.keys():
            raise KeyError
        del tasks[id]

    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=2)


def list_all_task():
    with open('tasks.json') as f:
        tasks = json.load(f)
        if len(tasks) == 0:
            print("No tasks in the list.")
            return

        for task_id, task_info in tasks.items():
            print(f"Task ID: {task_id}, Description: {task_info['description']}")


def list_task_by_status(status: str):
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
        cnt = 0
        for task_id, task_info in tasks.items():
            if task_info['status'] == status:
                cnt += 1
                print(f"Task ID: {task_id}, Description: {task_info['description']}")
        if cnt == 0:
            print(f"No tasks with status \'{status.title()}\'.")