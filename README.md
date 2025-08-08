# Task-Tracker
A task tracker to manage tasks, using command-line utility implemented in Python.  
This project idea has been selected from <a>https://roadmap.sh/projects/task-tracker</a>.

## Functionality:
You can have your tasks categorised into 'todo', 'in-progress' and 'done'. All tasks are stored in a JSON filed named 'tasks.json'. </br>
Every task in the file is stored as: </br>
```
  {
    "<id_of_the_task" : {
      "status": ["todo", "in-progress", "done"]
      "description: "<short_description_of_task>"
      "createdAt": "<timestamp_when_task_was_created>"
      "updatedAt": "<timestamp_when_task_was_updated>"
      }
  }
```
### This repository contains two files 'fucnctions.py' and 'taskCLI.py'.
functions.py: Contains all function definitions. </br>
taskCLI.py: Contains the working of command-line utility.

## Usage of CLI:
All commands are to be written in the terminal having the location of the directory containing the files 'functions.py' and 'taskCLI.py'

--> Add a new task: </br>
python taskCLI.py add -d <short_description_of_the_task> </br>
  #OR </br>
python taskCLI.py add --description <short_description_of_the_task> </br>

--> Mark a task as 'done': </br>
python taskCLI.py mark-done -i <id_of_the_task> </br>
  #OR </br>
python taskCLI.py mark-done --id <id_of_the_task> </br>

--> Mark a task as 'in-progress': </br>
python taskCLI.py mark-in-progress -i <id_of_the_task> </br>
  #OR </br>
python taskCLI.py mark-in-progress --id <id_of_the_task> </br>

--> Update description of the task: </br>
python taskCLI.py update -i <id_of_the_task> -d <new_short_description_of_the_task> </br>
  #OR </br>
python taskCLI.py update --id <id_of_the_task> --description <new_short_description_of_the_task> </br>

--> Delete a task: </br>
python taskCLI.py delete -i <id_of_the_task> </br>
  #OR </br>
python taskCLI.py delete --id <id_of_the_task> </br>
