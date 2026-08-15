import os


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_header(header_title):
    pass


class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title):
        self.__tasks.append({"title": title, "is_completed": False})

    def remove_task(self, task_index):
        self.__tasks.pop(task_index - 1)

    def get_task(self):
        return self.__tasks

    def get_task_by_id(self, task_index):
        return self.__tasks[task_index - 1]["title"]

    def complete_task(self, task_index):
        self.__tasks[task_index - 1]["is_completed"] = True

    def edit_task(self, task_index, new_title):
        self.__tasks[task_index - 1]["title"] = new_title

    def show_menu(self):
        print("\n==========TODO LIST==========\n")
        print("[1] View Task")
        print("[2] Add Task")
        print("[3] Remove Task")
        print("[4] Edit Task")
        print("[5] Complete Task")
        print("[0] Exit")
        print("\n-----------------------------")


task_manager = TaskManager()

while True:
    task_manager.show_menu()
    choice = int(input("\n>> Choice : "))

    match choice:
        case 1:
            print()
            for index, task in enumerate(task_manager.get_task(), start=1):
                if task["is_completed"]:
                    status_icon = "✅"
                else:
                    status_icon = "❌"
                print(f"{index}. [{status_icon}] {task["title"]}")

            input("\nPress Enter to continue...")

        case 2:
            task_count = int(input("\nEnter the number of tasks to add: ")) # ✅ ❌

            for index in range(task_count):
                title = input(f"Task {index + 1} : ")
                task_manager.add_task(title)            

        case 3:
            print()
            for index, task in enumerate(task_manager.get_task(), start=1):
                if task["is_completed"]:
                    status_icon = "✅"
                else:
                    status_icon = "❌"
                print(f"{index}. [{status_icon}] {task["title"]}")

            selected_index = int(input("\nEnter task number to remove : "))
            task_manager.remove_task(selected_index)

        case 4:
            print()
            print("Your Tasks:\n")

            for index, task in enumerate(task_manager.get_task(), start=1):
                if task["is_completed"]:
                    status_icon = "✅"
                else:
                    status_icon = "❌"
                print(f"{index}. [{status_icon}] {task["title"]}")

            print("\n----------------------------------\n")
            selected_index = int(input("Enter task ID to edit : "))

            print("\nCurrent Task :")
            print(f"{task_manager.get_task_by_id(selected_index)} \n")
            new_title = input("New task title : ")

            task_manager.edit_task(selected_index, new_title)

            print("\n✓ Task updated successfully!\n")
            input("Press Enter to continue...")

        case 5:
            is_completing_tasks = True

            while is_completing_tasks:
                print()
                for index, task in enumerate(task_manager.get_task(), start=1):
                    if task["is_completed"]:
                        status_icon = "✅"
                    else:
                        status_icon = "❌"
                    print(f"{index}. [{status_icon}] {task["title"]}")
                
                selected_index = int(input("\nEnter the task number to complete: "))
                task_manager.complete_task(selected_index)

                while True:
                    continue_input = input("Any other tasks to complete? (y/n): ").lower()

                    if len(continue_input) == 1 and continue_input in ("y", "n"):
                        if continue_input == "y":
                            break
                        else:
                            is_completing_tasks = False
                            break

                    print("Please enter only 'y' or 'n'.")
            
        case 0:
            print("\nGood Bye!")
            break

    clear_terminal()
