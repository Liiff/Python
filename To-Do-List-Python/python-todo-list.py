import os

task_list = []

def add_list(name):
    global task_list
    task_list.append(name)

def remove_list():
    pass

def show_menu():
    pass

while True:
    print("\n==========TODO LIST==========\n")
    print("[1] Lihat Task")
    print("[2] Tambah Task")
    print("[3] Hapus Task")
    print("[0] Keluar")
    print("\n-----------------------------")

    choice = int(input("\n>> Pilihan : "))

    match choice:
        case 1:
            print()
            for i, task in enumerate(task_list, start=1):  
                print("{i}. {task}")

            input("\nTekan Enter untuk lanjut...")

        case 2:
            name_list = input("Masukkan nama list : ")
            add_list(name_list)            

        case 3:
            pass

        case 0:
            break
            pass

    os.system("clear")
