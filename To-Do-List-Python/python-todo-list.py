import os

class Task:
    def __init__(self):
        self.__task_list = []

    def add_task(self, name):
        self.__task_list.append(
            {"name": name, "status": False}
        )

    def remove_task(self, no):
        self.__task_list.pop(no-1)

    def get_task(self):
        return self.__task_list

    def complete_task(self, no):
        self.__task_list[no-1]["status"] = True

    def show_menu(self):
        print("\n==========TODO LIST==========\n")
        print("[1] View Task")
        print("[2] Add Task")
        print("[3] Remove Task")
        print("[4] Complete Task")
        print("[0] Exit")
        print("\n-----------------------------")


my_task = Task()

while True:
    my_task.show_menu()

    choice = int(input("\n>> Choice : "))

    match choice:
        case 1:
            print()
            for i, task in enumerate(my_task.get_task(), start=1):
                if task["status"]:
                    status = "✅"

                else:
                    status = "❌"

                print(f"{i}. {task["name"]} {status}")

            input("\nPress Enter to continue...")

        case 2:
            total = int(input("\nEnter the number of tasks to add: ")) # ✅ ❌

            for i in range(total):
                name = input(f"Task {i+1} : ")
                my_task.add_task(name)            

        case 3:
            number = int(input("\nEnter task number to remove: "))
            my_task.remove_task(number)

        case 4:
            status = True

            while status:
                print()
                for i, task in enumerate(my_task.get_task(), start=1):
                    if task["status"]:
                        status = "✅"
                
                    else:
                        status = "❌"
                
                    print(f"{i}. {task["name"]} {status}")
                
                number = int(input("\nEnter the task number to complete: "))
                my_task.complete_task(number)

                while True:
                    exit = input("Any other tasks to complete? (y/n): ").lower()

                    if len(exit) == 1 and exit in ("y", "n"):
                        if exit == "y":
                            break

                        else:
                            status = False
                            break

                    print("Please enter only 'y' or 'n'.")
            
        case 0:
            print("\nGood Bye!")
            break

    os.system("cls")
