"No bloated codes, just a simple task manager. Thinking of using CSV and Json and not a database."
from json import loads
from os import path, makedirs
import sys
#from sys import argv #TODO

#Reading the config file from $HOME/.config/YATM/config.json
#If the file is not found a default one will be loaded.

#Checks if the config file exists.

__options__ = {
        "E":"EDIT",
        "A":"ADD",
        "R":"REMOVE",
        "L":"LIST",
        "D":"DESCRIBE",
        "H":"HELP",
        "Q":"QUIT"}


def print_options():
    "Prints the options and returns the user's choice."
    "In case of an invalid option, it will ask again."
    print("Options:")
    for option in __options__.values():
        print("\t" + "[{}]".format(option[0].upper()) + option[1:])

    choice = input("Choose an option: ").upper()
    if choice in __options__:
        return __options__[choice]
    else:
        print("Invalid option.")
        print_options()

#Getting the task files (.tasks) from a directory.
def find_task_files(directory):
    "Returns a list of the task files in the given directory."
    "If the directory is not found, it will return an empty list."
    if path.isdir(directory):
        return [file for file in path.listdir(directory) if file.endswith(".tasks")]
    else:
        return []


if path.isfile(path.expanduser("~/.config/YATM/config.json")):
    with open(path.expanduser("~/.config/YATM/config.json")) as config:
        config = loads(config.read())
else:
    #If the config file is not found, a default one will be created.
    #TODO Create a default config file.
    pass

#Parsing the config file.
Tasks = config["Tasks"]
print("Tasks found: ")
count = 0
task_list = list(Tasks.keys())

for task in task_list:
    print("\t" + "[{}]".format(count) + task)
    count += 1

current_task = int(input("Task number: "))

if current_task > count:
    print("Task not found.")
    #TODO Add a way to create a new task.
else:
    print(task_list[current_task])
    directory = Tasks[task_list[current_task]]["Directory"]
    choice = print_options()


    #Editing the config of a task.
    def edit_details(key, value):
        "Edits the description of a task."
        if key not in Task[task_list[current_task]]:
            sys.stderr("No such key found.")
        else:
            task[key] = value
        return task

    def add_tasks(directory, task_name, task_description):
        "Creates a file in the given directory with the given name, with extension .tasks"
        "If the directory does not exist, it will be created."
        if not path.isdir(directory):
            makedirs(directory)
        with open(path.expanduser(directory + "/" + task_name + ".tasks"), "w") as task_file:
            task_file.write(task_description)

    if choice == "EDIT":
        #TODO Edit the task.
        pass
    elif choice == "ADD":
        #TODO Add a new task.
        add_tasks(directory, input("Task name: "), input("Description: "))

    elif choice == "REMOVE":
        #TODO Remove the task.
        pass
    elif choice == "LIST":
        #TODO List all the tasks.
        pass
    elif choice == "DESCRIBE":
        #TODO Describe the task.
        pass
    elif choice == "HELP":
        #TODO Print the help.
        pass
    elif choice == "QUIT":
        #TODO Quit the program.
        pass
    else:
        #Already handled.
        pass




