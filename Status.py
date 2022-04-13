"""Tasks: A simple task manager which allows you to add, delete, and view tasks.
Each task has a name, a description, a priority, a type, and a due date.
A type has a color, a priority, and a description.
"""

# We fetch the config file from the config directory which is $HOME/.config/YATM/config.json
import os
import json
from os import path

with open(path.expanduser("~/.config/YATM/config.json")) as config_file:
    config = json.load(config_file)

# Data-dir is defined in the config file, but the default is $HOME/.YATM/

if "data-dir" in config:
    data_dir = config["data-dir"]
else:
    data_dir = path.expanduser("~/.YATM/")

# We create the data-dir if it doesn't exist
if not path.exists(data_dir):
    os.makedirs(data_dir)

""" # We check if type.json exists in the data-dir
    if not path.exists(data_dir + "/type.json"):
        # If it doesn't exist, we create an empty type.json
        with open(data_dir + "/type.json", "w") as type_file:
            json.dump({} , type_file)
    
    # We import the tasks from the data-dir
    with open(data_dir + "/type.json") as type_file:
        tasks = json.load(type_file)
"""


# We scan the data_dir for any folders.
# Each type has a folder with the same name as the task, and stores the task's files.


type_list = dict()
error_list = list()

for entries in os.scandir(data_dir):
    if entries.is_dir():
        # We check the folder contains config.json
        if path.exists(entries.path + "/config.json"):
            # We load the config.json
            with open(entries.path + "/config.json") as config_file:
                config = json.load(config_file)
                # We append the task to the type_list
                type_list[entries.name] = config
        else:
            # If the folder doesn't contain config.json, we add it to the error_list
            error_list.append(entries.name)

# We print the type_list and error_list in a colored format.
# The error_list is printed in red.
# The type_list is printed in the colour type_list[type]["color"]

import colorama
from colorama import Fore, Back, Style
print(Fore.RED + "The following types are missing config.json:")
print(Fore.RED + str(error_list))
print(Style.RESET_ALL)


print(Fore.GREEN + "The following types are available:")
for type in type_list:
    print(Fore.GREEN + type + ": " + Fore.WHITE + type_list[type]["Description"])
print(Style.RESET_ALL)

__commands__ = ["add", "delete", "view", "edit", "help"]

def get_help():
    print(Fore.YELLOW + "YATM : Yet Another Task Manager" + Style.RESET_ALL)

    print(Fore.YELLOW + "Commands:" + Style.RESET_ALL)
    
    print(Fore.BLACK + "------------------------------------------------------" + Style.RESET_ALL)

    print(Fore.GREEN + "add <name> <description> <priority> <type> <due date>" + Style.RESET_ALL)
    print("Adds a task with the given name, description, priority, type, and due date.")
    print("If the task already exists, it will be overwritten.")
    
    print(Fore.BLACK + "------------------------------------------------------" + Style.RESET_ALL)

    print(Fore.BLUE + "delete <name>" + Style.RESET_ALL)
    print("Deletes the task/type with the given name.")
    
    print(Fore.BLACK + "------------------------------------------------------" + Style.RESET_ALL)

    print(Fore.LIGHTRED_EX + "view <name>" + Style.RESET_ALL)
    print("Views the summary of the task/type with the given name.")
    
    print(Fore.BLACK + "------------------------------------------------------" + Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX + "edit <task/type> <name> <key:value>" + Style.RESET_ALL)
    print("Updates the task/type with the given name with the given values.")
    print("The key:value pairs are separated by a colon.")

    print(Fore.BLACK + "------------------------------------------------------" + Style.RESET_ALL)

    print(Fore.CYAN + "help" + Style.RESET_ALL)
    print("Shows this help message.")
    
    print(Fore.BLACK + "------------------------------------------------------" + Style.RESET_ALL)
    
    print(Fore.CYAN + "Name of a task is in the format <type>/<task_name>" + Style.RESET_ALL)

    print(Fore.BLACK + "------------------------------------------------------" + Style.RESET_ALL)
command = input("Enter a command (help to view help: ")
if command == "help":
    get_help()
