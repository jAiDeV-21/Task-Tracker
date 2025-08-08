# Task-Tracker
A task tracker to manage tasks, using command-line utility implemented in Python.

## Functionality:
You can have your tasks categorised into 'todo', 'in-progress' and 'done'. All tasks are stored in a JSON filed named 'tasks.json'.
Every task in the file is stored as:
  {
    "<id_of_the_task" : {
      "status": ["todo", "in-progress", "done"]
      "description: "<short_description_of_task>"
      "createdAt": "<timestamp_when_task_was_created>"
      "updatedAt": "<timestamp_when_task_was_updated>"
      }
  }

### This repository contains two files 'fucnctions.py' and 'taskCLI.py'.
functions.py: Contains all function definitions.
taskCLI.py: Contains the working of command-line utility.

## Usage of CLI:
All commands are to be written in the terminal having the location of the directory containing the files 'functions.py' and 'taskCLI.py'

--> Add a new task:
python taskCLI.py add -d <short_description_of_the_task>
  OR
python taskCLI.py add --description <short_description_of_the_task>

--> Mark a task as 'done':
python taskCLI.py mark-done -i <id_of_the_task>
  OR
python taskCLI.py mark-done --id <id_of_the_task>

--> Mark a task as 'in-progress':
python taskCLI.py mark-in-progress -i <id_of_the_task>
  OR
python taskCLI.py mark-in-progress --id <id_of_the_task>

--> Update description of the task:
python taskCLI.py update -i <id_of_the_task> -d <new_short_description_of_the_task>
  OR
python taskCLI.py update --id <id_of_the_task> --description <new_short_description_of_the_task>

--> Delete a task:
python taskCLI.py delete -i <id_of_the_task>
  OR
python taskCLI.py delete --id <id_of_the_task>
