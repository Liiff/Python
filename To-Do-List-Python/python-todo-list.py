import os

task_list = []
status = True

def add_list(name):
    global task_list
    task_list.append(name)

def remove_list():
    pass

while status:
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
            for task in range(len(task_list)):  
                print(f"{task+1}. {task_list[task]}")

            input("\nTekan Enter untuk lanjut...")

        case 2:
            name_list = input("Masukkan nama list : ")
            add_list(name_list)            

        case 3:
            pass

        case 0:
            pass

    os.system("clear")
