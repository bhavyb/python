dataset = []
dataset_summary = []

def input_data():
    global dataset
    raw = input("\nEnter Data for 1D array (seperated by sapce): ")
    dataset = [float(i) for i in raw.split()]
    print("Data has been stored successfully!\n")

def display_summary():
    if not dataset:
        print("\nNo data available. Please input data first.\n")
        return

    total_element = len(dataset)
    min_value = min(dataset)
    max_value = max(dataset)
    total_sum = sum(dataset)
    average = total_sum / total_element
    
    global dataset_summary
    dataset_summary = {
        "total_element": total_element,
        "min": min_value,
        "max": max_value,
        "sum": total_sum,
        "average": average
    } 

    print("\nData Summary (Buil-in Funcions:)")
    print("Total elements: ", total_element)
    print("Minmum value: ",min_value)
    print("Maximum value: ",max_value)
    print("Sum of all value: ",max_value)
    print("Average value: ",max_value)
    print()

def factorial(n):
    if n < 0:
        print("\nFactorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def calculate_factorial():
    n = int(input("Enter a number to calculate its factorial: "))
    result = factorial(n)
    if result is not None:
        print(f"Factorial of {n} is: {result}\n")

def filter_by_threshold():
    if not dataset:
        print("\nNo data available. Please input data first.")
        return
    
    threshold = float(input("\nEnter the threshold value to filter out data above this value: "))
    filtered = list(filter(lambda x: x >= threshold, dataset))

    print(f"Filtered Data (values >= {threshold}):")
    if filtered:
        print(" ".join(str(i) for i in filtered))
        
    else:
        print("\nNo values meet the condition\n")
def sort_1d_list(list, ascending = True):
    return sorted(list, reverse=not ascending)

def sort_2d_rows(matrix, ascending = True):
    return [sorted(row, reverse=not ascending)for row in matrix]

def sort_data_menu():
    print("\nSort Options:")
    print("1. Sort current 1D dataset")
    print("2. Sort row of 2D list (manual input)")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        if not dataset:
            print("\nNo data available. Please input data first.\n")
            return

        print("\nChoose sorting order: \n1. Ascending\n2. Descending")
        order = input("Enter your choice: ")
        ascending = (order == "1")
        
        sorted_data = sort_1d_list(dataset, ascending=ascending)
        direction = "Ascending" if ascending else "Descending"
        print(f"\nSorted Data in {direction} Order:")
        print(" ".join(str(x) for x in sorted_data))

    elif choice == 2:
        rows = int(input("Enter the number of the rows :: "))
        cols = int(input("Enter the number of the columns :: "))

        matrix = []
        print("Enter rows, values seprated by spaces: ")
        for i in range(rows):
            rows_raw = input(f"Row {i+1}: ")
            parts = rows_raw.split()

            while len(parts) != cols:
                print(f"Please Enter exactly {cols} values:")
                rows_raw = input(f"Row {i+1}:")
                parts = rows_raw.split()
            row = [float(i) for i in parts]
            matrix.append(row)

            print("\nChoose sorting order for each row:\n1. Ascending\n2. Descending")
            order = int(input("\nEnter your Choice: "))
            ascending = (order != 1)
            
            sorted_matrix = sort_2d_rows(matrix, ascending=ascending)
        print("\nSorted 2D List (each row):")
        for row in sorted_matrix:
            print(" ".join(str(x) for x in row))
    else:
        print("Invalid choice.")


def dataset_stats():
    mn = min(dataset)
    mx = max(dataset)
    total = sum(dataset)
    avg = total / len(dataset)
    return mn, mx, total, avg


def display_dataset_stats_menu():
    if not dataset:
        print("No data available. Please input data first.")
        return
    mn, mx, total, avg = dataset_stats()
    print("Dataset Statistics (Return Multiple Values):")
    print(f"- Minimum value: {mn}")
    print(f"- Maximum value: {mx}")
    print(f"- Sum of all values: {total}")
    print(f"- Average value: {avg:.2f}\n")

def main():
    print("Welcome to the Data Analyzer and Transformer program")
    while  True:
        print("Main Menu")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in function)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lamda function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple value)")
        print("7. Exit Program")
        
        choice = int(input("Please Enter your Choice: "))
        
        if choice == 1:
            input_data()
        elif choice == 2:
            display_summary()
        elif choice == 3:
            calculate_factorial()
        elif choice == 4:
            filter_by_threshold()
        elif choice == 5:
            sort_data_menu()
        elif choice == 6:
            display_dataset_stats_menu()
        elif choice == 7:
            print("\nThank you for using Data Anlyzer and Transformer Program. Goodbye!\n")
            exit()
        else:
            print("Invaild Choice.....\n")
            
if __name__ == "__main__":
    main()