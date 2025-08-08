from argparse import ArgumentParser, Namespace
from functions import add_task, mark_task_done, mark_task_in_progress, update_task, delete_task, list_task_by_status, list_all_task

parser = ArgumentParser()

parser.add_argument('status', help='Status of the task', type=str,
                    choices=['add', 'update', 'delete', 'mark-done', 'mark-in-progress',
                             'list-todo', 'list-done', 'list-in-progress'])
parser.add_argument('-i', '--id', help='Id of the task', type=int)
parser.add_argument('-d', '--description', help='Short description of the task', type=str)
args: Namespace = parser.parse_args()

match args.status:
    case 'add':
        try:
            if args.id is not None:
                raise ValueError
            if args.description is None:
                raise NameError
            id = add_task('todo', args.description)
            print(f"Task added successfully. (ID={id}).")
        except ValueError as e:
            print("\'add\' does not accept 'id' as argument.")
        except NameError as e:
            print("'\add' requires description of the task.")
    case 'mark-in-progress':
        try:
            if args.description is not None:
                raise NameError
            mark_task_in_progress('in-progess', str(args.id))
            print(f'Complete the task. (ID={args.id})')
        except KeyError as e:
            print('Invalid task ID.')
        except NameError as e:
            print("\'mark-in-progress\' only accepts \'id\'.")
    case 'mark-done':
        try:
            if args.description is not None:
                raise NameError
            mark_task_done('done', str(args.id))
            print(f'Task completed. (ID={args.id})')
        except KeyError as e:
            print('Invalid task ID.')
        except NameError as e:
            print("\'mark-in-progress\' only accepts \'id\'.")
    case 'update':
        try:
            if args.description is None:
                raise NameError
            update_task(args.description, str(args.id))
            print(f'Task updated successfully. (ID={args.id})')
        except KeyError as e:
            print('Invalid task ID.')
        except NameError as e:
            print("\'descritpion\' should not be empty.")
    case 'delete':
        try:
            delete_task(str(args.id))
            print(f'Task deleted successfully. (ID={args.id})')
        except KeyError as e:
            print('Invalid task ID.')
    case 'list-all':
        list_all_task()
    case 'list-todo' | 'list-done' | 'list-in-progress':
       list_task_by_status(args.status[5:])
    case _:
        print('Invalid choice')
