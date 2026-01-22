import numpy as np

class DataAnalytic:
    """NumPy Analyzer Toolkit using OOP"""
    
    def __init__(self):
        self.array = None
        
    def create_array(self):
        print("\nSelect the type of array to create: ")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of elements: "))
            data = list(map(int, input("Enter elements: ").split()))
            if len(data) < n:
                print("Error: Not enough elements!")
                return
            self.array = np.array(data[:n])
            
        elif choice == 2:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            data = list(map(int, input("Enter elements separated by space: ").split()))
            if len(data) != r * c:
                print(f"Error: Enter exactly {r * c} elements.")
                return
            self.array = np.array(data).reshape(r, c)
            
        elif choice == 3:
            d = int(input("Enter depth: "))
            r = int(input("Enter rows: "))
            c = int(input("Enter columns: "))
            data = list(map(int, input("Enter elements separated by space: ").split()))
            if len(data) != d * r * c:
                print(f"Error: Enter exactly {d * r * c} elements.")
                return
            self.array = np.array(data).reshape(d, r, c)

        else:
            print("Invalid choice!")
            return
        
        print("Array created successfully")
        print(self.array)

    def indexing_slicing(self):
        if self.array is None:
            print("Create an array first!")
            return
        
        print("\nChoose an operation: ")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            idx = tuple(map(int, input("Enter index (space separated): ").split()))
            print("Result:", self.array[idx])
        
        elif choice == 2:
            if self.array.ndim != 2:
                print("Slicing supported only for 2D arrays.")
                return
            r1, r2 = map(int, input("Enter row range (start:end): ").split(":"))
            c1, c2 = map(int, input("Enter column range (start:end): ").split(":"))
            print("\nSliced Array:")
            print(self.array[r1:r2, c1:c2])

    def mathematical_operations(self):
        if self.array is None:
            print("Create an array first!")
            return
        
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice: "))

        data = list(map(int, input(
            f"Enter same-size array elements ({self.array.size} elements): ").split()))

        if len(data) != self.array.size:
            print("Error: Array size mismatch!")
            return

        arr2 = np.array(data).reshape(self.array.shape)

        if choice == 1:
            result = self.array + arr2
        elif choice == 2:
            result = self.array - arr2
        elif choice == 3:
            result = self.array * arr2
        elif choice == 4:
            result = self.array / arr2
        else:
            print("Invalid choice!")
            return
        
        print("\nResult:")
        print(result)

    def combine_split(self):
        if self.array is None:
            print("Create an array first!")
            return
        
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = list(map(int, input(
                f"Enter elements of another array ({self.array.size} elements): ").split()))

            if len(data) != self.array.size:
                print("Error: Size mismatch!")
                return

            arr2 = np.array(data).reshape(self.array.shape)
            combined = np.concatenate((self.array, arr2), axis=0)
            print("\nCombined Array:")
            print(combined)

        elif choice == 2:
            parts = int(input("Enter number of splits: "))
            split_array = np.array_split(self.array, parts)
            print("\nSplit Arrays:")
            for arr in split_array:
                print(arr)

    def search_sort_filter(self):
        if self.array is None:
            print("Create an array first!")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            val = int(input("Enter value to search: "))
            result = np.where(self.array == val)
            print("Found at index:", result)

        elif choice == 2:
            print("\nSorted Array:")
            print(np.sort(self.array))

        elif choice == 3:
            condition = int(input("Show value greater than: "))
            print(self.array[self.array > condition])

    def aggregates_statistics(self):
        if self.array is None:
            print("Create an array first!")
            return

        print("\nChoose an operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sum:", np.sum(self.array))
        elif choice == 2:
            print("Mean:", np.mean(self.array))
        elif choice == 3:
            print("Median:", np.median(self.array))
        elif choice == 4:
            print("Standard Deviation:", np.std(self.array))
        elif choice == 5:
            print("Variance:", np.var(self.array))

    @classmethod
    def project_info(cls):
        print("\nNumpy Analyzer Project")
        
    @staticmethod
    def exit_program():
        print("\nThank you for using the NumPy Analyzer. Goodbye!")
        exit()

def main():
    analyzer = DataAnalytic()
    DataAnalytic.project_info()

    while True:
        print("\n" + "=" * 40)
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Indexing and Slicing")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            analyzer.create_array()
        elif choice == 2:
            analyzer.mathematical_operations()
        elif choice == 3:
            analyzer.combine_split()
        elif choice == 4:
            analyzer.search_sort_filter()
        elif choice == 5:
            analyzer.aggregates_statistics()
        elif choice == 6:
            analyzer.indexing_slicing()
        elif choice == 7:
            DataAnalytic.exit_program()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
