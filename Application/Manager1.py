def Manager_menu():
    print("\t\t\t\t\t----Manager Menu----")
    print("--"*30)
    print("1. View My Profile")
    print("2. Edit My Profile")
    print("3. View Employees")
    print("4. Delete Employee Profiles")
    print("5. Exit")
    print("--"*30)
    
    def choice():
        choice1 = int(input("Enter your choice: "))
        if choice1 == 1:
            manager_profile_view()
        elif choice1 == 2:
            Edit_manager_profile()
        elif choice1 == 3:
            view_employees()
        elif choice1 == 4:
            delete_employee_profiles()
        elif choice1 == 5:
            print("Back to main menu")
            from Application.MenuFile import menu
            menu()
        else:
            print("Wrong Choice Please enter a valid choice.")
            choice()
    choice()


def manager_profile_view():
    pass

def Edit_manager_profile():
    pass

def view_employees():
    pass

def delete_employee_profiles():
    pass