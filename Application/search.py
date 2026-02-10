def ChangeMenu():
    print("----Others Profile----")
    print("1.Manager")
    print("2.Employee")
    print("3.Back to Boss menu")
    print("--"*30)
    profile = input("Who do you want to change?:")
    def choice():
        if profile == "1":
            choice1()
        elif profile == "2":
            choice2()
        elif profile == "3":
            from Application.Boss1 import boss_menu
            boss_menu()
        else:
            print("Wrong Choice Please enter a valid choice.")
            choice()
    choice()

def choice1():
    print("----Change Manager----")
    print("1.View manager profile")
    print("2.Make Changes")
    print("3.Go back to menu")
    print("--"*30)
    def managerchoice():
        select = int(input("Enter your choice:"))
        if select == 1:
            with open("Manager.txt", "r") as M:
                lines = M.readlines()
                print("----Details----")
                print("Name:", lines[0], end="")
                print("Password:", lines[1], end="")
                print("Address:", lines[2], end="")
                print("Phone:", lines[3], end="")
                print("Email:", lines[4], end="")
                print("--" * 30)
                choice1()
        elif select == 2:
            def Edit_choice():
                print("----Edit Profile----")
                pass
        elif select == 3:
            ChangeMenu()
        else:
            print("You have entered wrong choice.")
            print("--" * 30)
            managerchoice()

def choice2():
    print("----Employee details----")
    print("1.View employees")
    print("2.Delete employee profile")
    print("Go back to menu")
    print("--"*30)