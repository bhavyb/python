import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None
        print("Sales Data Analyzer initialized.")

    def __del__(self):
        print("Cleaning up resources...")

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print("Error loading dataset: ", e)

    def explore_data(self):
        if self.data is None:
            print("Load data first.")
            return
        
        print("\n1.Display the First 5 rows\n2.Display the Last 5 rows\n3.Display Columns\n4.Display Data Types\n5.Display basic Info")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            print(self.data.head())
        elif choice == 2:
            print(self.data.tail())
        elif choice == 3:
            print(self.data.columns)
        elif choice == 4:
            print(self.data.dtypes)
        elif choice == 5:
            print(self.data.info())
        else:
            print("Invalid choice")

    def clean_data(self):
        if self.data is None:
            print("Load data first")
            return

        print("\n1. Show missing values\n2. Fill with mean\n3. Drop rows\n4. Replace with value")
        
        choice = int(input("Enter Choice: "))

        if choice == 1:
            print(self.data.isnull().sum())
        elif choice == 2:
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing value filled eith mean.")
        elif choice == 3:
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped.")
        elif choice == 4:
            value = input("Enter replacement value: ")
            self.data.fillna(value, inplace=True)
            print("missing values replaced")
        else:
            print("Invalied choice")


    def mathematical_operations(self):
        if self.data is None:
            print("Load data first")
            return
        
        numeric_cols = self.data.select_dtypes(include=np.number)
        print("Sum:\n",numeric_cols.sum())
        print("\nMean:\n",numeric_cols.mean())

    def combine_data(self, other_df):
        self.data = pd.concat([self.data, other_df], ignore_index=True)
        print("Data combined successfully")

    def solit_data(self, column):
        if column not in self.data.columns:
            print("Invalied column")
            return
        
        group = dict(tuple(self.data.groupby(column)))
        print(f"Data split into {len(group)} groups.")
        return group

    def search_sort_filter(self):
        if self.data is None:
            print("Load data first")
            return
        
        print("\n1. Search\n2. Sort\n3. Filter")
        choice = int(input("Enter choice: "))

        if choice == 1:
            col = input("Column name: ")
            val = input("Value: ")
            print(self.data[self.data[col].astype(str).str.contains(val, case=False)])
        elif choice == 2:
            col = input("Sort by column: ")
            print(self.data.sort_values(by=col))
        elif choice == 3:
            col = input("Filter column: ")
            val = input("Filter value: ")
            print(self.data[self.data[col].astype(str).str.contains(val, case=False)])
        else:
            print("Invalied choice")

    def aggregate_functions(self):
        if self.data is None:
            print("Load data first")
            return
        
        print(self.data.agg(['sum', 'mean', 'count'], numeric_only=True))

    def statistical_analysis(self):
        if self.data is None:
            print("Load data first")
            return
        
        print(self.data.describe())
        print("\nStandard Deviation: \n", self.data.std(numeric_only=True))
        print("\nVariance: \n", self.data.var(numeric_only=True))

    def create_pivot_table(self):
        if self.data is None:
            print("Load data first")
            return

        pivot = pd.pivot_table(
            self.data,
            values='Sales',
            index='Region',
            columns='Product',
            aggfunc='sum'
        )

        print("\nPivot Table:\n", pivot)
        return pivot

        
    def visualize_data(self):
        if self.data is None:
            print("Load data first")
            return
        
        print("""
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Plot
5. Histogram Plot
6. Stack Plot
        """)
        
        choice = int(input("Enter choice: "))

        if choice == 1:
            self.data.groupby("Region")["Sales"].sum().plot(kind='bar')
        elif choice == 2:
            self.data.plot(x = 'Year', y = 'Sales')
        elif choice == 3:
            plt.scatter(self.data['Year'], self.data['Sales'])
        elif choice == 4:
            self.data.groupby("Product")["Sales"].sum().plot(kind='pie', autopct='%1.1f%%')
        elif choice == 5:
            self.data['Sales'].hist()
        elif choice == 6:
            pivot = self.data.pivot_table(values='Sales', index='Year', columns='Region', aggfunc='sum')
            pivot.plot.area()
        else:
            print("Invalied choice")
            return
        
        plt.title("Sales Visualiztion")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.show()
        
    def seaborn_visulization(self):
        if self.data is None:
            print("Load data first")
            return
        
        sns.boxenplot(
            x='Region',
            y='Sales',
            data=self.data,
            palette='Set2'
        )   

        plt.title("Sales Distribution by Region")
        plt.show()
        

    def save_visulization(self, filename):
        plt.savefig(filename)
        print(f"Visualization saved as {filename}")

def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("""
========= Data Analysis & Visualization Program =========
Please select an option
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
=========================================================
        """)
            
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n== Load Datadet ==")
            path = input("Enter the CSV file path: ")
            analyzer.load_data(path)

        elif choice == 2:
            print("== Explore Data")
            analyzer.explore_data()

        elif choice == 3:
            analyzer.mathematical_operations()
            analyzer.search_sort_filter()
            analyzer.aggregate_functions()

        elif choice == 4:
            analyzer.clean_data()
            
        elif choice == 5:
            analyzer.statistical_analysis()
            analyzer.create_pivot_table()

        elif choice == 6:
            analyzer.visualize_data()
            analyzer.seaborn_visulization()

        elif choice == 7:
            print("== Save Visualization ==")
            name = input("Enter filenae (eg. plot.png)")
            analyzer.save_visulization(name)
            print(f"Visulization saved as {name} successfully!")

        elif choice == 8:
            print("Exiting the program. Goodbye!")
            sys.exit()

        else:
            print("Invalied option")

if __name__ == "__main__":
    main()
