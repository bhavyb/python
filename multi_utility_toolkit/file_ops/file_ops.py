def create_file():
    name = input("File name: ")
    open(name, "w").close()
    print("File created successfully")
    print("==============================")


def write_file():
    name = input("File name: ")
    data = input("Enter data: ")
    with open(name, "w") as f:
        f.write(data)
    print("Data written successfully")
    print("==============================")


def read_file():
    name = input("File name: ")
    with open(name, "r") as f:
        print("File content: \n", f.read())
    print("==============================")


def append_file():
    name = input("File name: ")
    data = input("Enter data: ")
    with open(name, "a") as f:
        f.write("\n" + data)
    print("Data appended successfully")
    print("==============================")


def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create file")
        print("2. Write file")
        print("3. Read file")
        print("4. Append file")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")
        if ch == "1":
            create_file()
        elif ch == "2":
            write_file()
        elif ch == "3":
            read_file()
        elif ch == "4":
            append_file()
        elif ch == "5":
            break