def boss_menu():                       # Menu for boss
    print("\t\t\t\t\t----Boss Menu----")
    print("--"*30)
    print("1. View My Profile")
    print("2. Edit My Profile")
    print("3. View Manager and Employees")
    print("4. Delete Profiles")
    print("5. Exit")
    print("--"*30)
    def choice():
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            boss_profile_view()
        elif choice1 == 2:
            Edit_boss_profile()
        elif choice1 == 3:
            from Application.search import ChangeMenu
            ChangeMenu()
        elif choice1 == 4:
            Delete_profiles()
        elif choice1 == 5:
            print("Back to main menu")
            from Application.MenuFile import menu
            menu()
        else:
            print("Wrong Choice Please enter a valid choice.")
            choice()
    choice()

def boss_profile_view():
    with open("Boss.txt", "r") as boss:
        lines = boss.readlines()
        print("\t\t\t\t\t----Details----")
        print("--"*30)
        print("Name:", lines[0], end="")
        print("Password:", lines[1], end="")
        print("Address:", lines[2], end="")
        print("Phone:", lines[3], end="")
        print("Email:", lines[4],)
        print("--" * 30)
        boss_menu()

def Edit_boss_profile():
    print("\t\t\t\t\t----Edit Menu----")
    print("--"*30)
    print("1.Edit Password")
    print("2.Edit Address")
    print("3.Edit Phone Number")
    print("4.Edit Email")
    print("5.Back to menu")
    print("--"*30)
    def newpass():
        new_password = input("Enter new password: ")
        Check = input("Reenter your new password: ")
        if Check == new_password:
            with open("Boss.txt", 'r') as boss:
                line = boss.readlines()
                if len(line) > 2:
                    line[1] = new_password + "\n"
            with open("Boss.txt", 'w') as boss:
                boss.writelines(line)
            print("Password Updated Successfully.")
        else:
            print("Wrong Password!")
            newpass()
        choice()
    def choice():
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            newpass()
        elif choice1 == 2:
            new_address = input("Enter new address: ")
            with open("Boss.txt",'r') as boss:
                line = boss.readlines()
                if len(line) >= 3:
                    line[2] = new_address + "\n"
            with open("Boss.txt",'w') as boss:
                boss.writelines(line)
            print("Address Updated Successfully.")
            choice()

        elif choice1 == 3:
            new_Phone = int(input("Enter new phone number: "))
            with open("Boss.txt",'r') as boss:
                line = boss.readlines()
                if len(line) > 4:
                    line[3] = new_Phone + "\n"
            with open("Boss.txt",'w') as boss:
                boss.writelines(line)
            print("Phone number Updated Successfully.")
            choice()

        elif choice1 == 4:
            new_Email = input("Enter new Email: ")
            with open("Boss.txt",'r') as boss:
                line = boss.readlines()
                if len(line) >= 5:
                    line[4] = new_Email + "\n"
            with open("Boss.txt",'w') as boss:
                boss.writelines(line)
            print("Email Updated Successfully.")
            choice()

        elif choice1 == 5:
            print("Going Back to Boss menu")
            boss_menu()

        else:
            print("Wrong Choice Please enter a valid choice.")
            choice()

def Delete_profiles():
    import os
    choice = input("Are you sure you want to delete the profiles? (y/n): :").lower()
    if choice == "y":
        os.remove("Boss.txt")
        print("Profile Deleted Successfully.")
        print("\t\t\t\t\t----New Profile----")
        print("--"*30)
        name = input("Enter your name: ") + "\n"
        password = input("Enter your password: ") + "\n"
        address = input("Enter address: ") + "\n"
        phone = int(input("Enter Phone Number: "))
        phone1 = str(phone) + "\n"
        email = input("Enter Email: ") + "\n"
        print("--"*30)
        with open("Boss.txt", 'w') as boss:
            boss.write(name)
            boss.write(password)
            boss.write(address)
            boss.write(str(phone1))
            boss.write(email)
    else:
        boss_menu()
