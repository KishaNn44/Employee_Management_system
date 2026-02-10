from Boss1 import boss_menu
from Manager1 import Manager_menu 
from employee import employee_menu
def menu():
    print("\t\t\t\t\t-----Menu-----")
    print("--"*30)
    print("Your Status at the company?")
    print("--"*30)
    print("\t1.Boss")
    print("\t2.Manager")
    print("\t3.Employee")
    print("\t4.Exit")
    print("--"*30)
    choice = int(input("Who do you want to login as?\n State: "))
    while True:
        if choice == 1:
            print("-"*30)
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print("-"*30)
            with open("Boss.txt", 'r') as boss:
                line = boss.readlines()
                store_user = line[0].strip()
                store_password = line[1].strip()
                if password == store_password and username == store_user:
                    boss_menu()
                else:
                    print("Invalid username or password")
        elif choice == 2:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print("-"*30)
            with open("Manager.txt", 'r') as manager:
                line = manager.readlines()
                store_user = line[0].strip()
                store_password = line[1].strip()
                if password == store_password and username == store_user:
                    print("Manager login successful.")
                    Manager_menu()
                else:
                    print("Invalid username or password")

        elif choice == 3:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            print("-"*30)
            with open("Employee.txt", 'r') as employee:
                line = employee.readlines()
                store_user = line[0].strip()
                store_password = line[1].strip()
                if password == store_password and username == store_user:
                    print("Employee login successful.")
                    employee_menu()
                else:
                    print("Invalid username or password")



        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Please Enter Correct choice.")
            menu()

    
menu()