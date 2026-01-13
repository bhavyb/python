from daterime_ops.datetime_tools import datetime_menu
from math_ops.math_tools import math_menu
from random_ops.random_tools import random_menu
from uuid_ops.uuid_tools import generate_uuid
from file_ops.file_ops import file_menu
from explorer.dir_explorer import explore_module

def main_menu():
    while True:
        print("\n==============================")
        print("Welcome to Multi Utility Toolkit")
        print("==============================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Modules Attributes (dir())")
        print("7. Exit")
        print("==============================")



        choice = int(input("Enter your choice: "))
        if choice == 1:
            datetime_menu()
        elif choice == 2:
            math_menu()
        elif choice == 3:
            random_menu()
        elif choice == 4:
            generate_uuid()
        elif choice == 5:
            file_menu()
        elif choice == 6:
            explore_module()
        elif choice == 7:
            print("==============================")
            print("Thank you for using the Multi-Utility Toolkit")
            print("==============================")
            break
        else:
            print("Please enter a valid choice")
            break

if __name__ == "__main__":
    main_menu()