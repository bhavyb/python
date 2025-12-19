print("Welcome to the Pattern Generator and Number Analyzer!\n")

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            r = int(input("Enter the number of rows for the pattern: "))
            print("Pattern")
            for i in range(1, r +1):
                print("*" * i)
        
        case 2:
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            sum = 0
            for i in range(start, end + 1):
                if i % 2 == 0:
                    print(f"Number {i} is Even")
                else:
                    print(f"Number {i} is Odd")
                sum += i
            print(f"Sum of all number from {start} to {end} is: {sum}")
            
        case 3:
            print("Exiting the program. Goodbye")
            exit()