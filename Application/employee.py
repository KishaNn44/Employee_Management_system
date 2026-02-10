def employee_menu():
    print("\t\t\t\t\t-----Employee Menu-----")
    print("--"*30)
    print("1. View Profile")
    print("2. Reset Password")
    print("3. Submit Suggestions")
    print("4. Enquiry ")
    print("5. Exit")
    print("--"*30)
    choice = int(input("Enter your choice: "))
    while True:
        if choice == 1:
            print("++++++++++ My Profile +++++++")
        elif choice == 2:
            print("++++++++++ Reset Password Pannel +++++++")
        elif choice == 3:
            print("++++++++++ Submit Suggestions +++++++")
        elif choice == 4:
            print("++++++++++ Enquiry Pannel +++++++")
            break
        elif choice == 5:
            print("Back to main menu")
            from Application.MenuFile import menu
            menu()
        else:
            print("Invalid choice. Please try again.")