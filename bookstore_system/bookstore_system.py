"""
Bookstore Inventory and Analytics System
Author: Bhavy Bhuva

This project follows the given instructions:
- Control Structures & Arrays
- OOP (Bookstore class)
- NumPy & Pandas for analysis
- Matplotlib & Seaborn for visualization
- Uses inventory.csv and sales.csv (auto-generated if not present)
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# FILE PATHS 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(BASE_DIR, "inventory.csv")
SALES_FILE = os.path.join(BASE_DIR, "sales.csv")

#  SAMPLE DATA 
def generate_sample_data():
    if not os.path.exists(INVENTORY_FILE):
        inventory_data = pd.DataFrame({
            "Title": ["Python Basics", "Data Science 101", "ML Guide", "AI Future"],
            "Author": ["John Doe", "Jane Smith", "Andrew Ng", "Elon Tech"],
            "Genre": ["Programming", "Data Science", "AI", "AI"],
            "Price": [350, 500, 650, 700],
            "Quantity": [20, 15, 10, 8]
        })
        inventory_data.to_csv(INVENTORY_FILE, index=False)

    if not os.path.exists(SALES_FILE):
        sales_data = pd.DataFrame({
            "Date": ["2025-01-05", "2025-01-10", "2025-02-01", "2025-02-15"],
            "Title": ["Python Basics", "Data Science 101", "ML Guide", "Python Basics"],
            "Quantity Sold": [5, 3, 4, 6],
            "Total Revenue": [1750, 1500, 2600, 2100]
        })
        sales_data.to_csv(SALES_FILE, index=False)

#  BOOKSTORE CLASS 
class Bookstore:
    def __init__(self):
        self.inventory = pd.read_csv(INVENTORY_FILE)
        self.sales = pd.read_csv(SALES_FILE)

    # INVENTORY METHODS
    def add_book(self, title, author, genre, price, quantity):
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive")
            return
        new_book = {
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Price": price,
            "Quantity": quantity
        }
        self.inventory = pd.concat([self.inventory, pd.DataFrame([new_book])], ignore_index=True)
        self.inventory.to_csv(INVENTORY_FILE, index=False)
        print("Book added successfully")

    def update_inventory(self, title, quantity):
        if quantity < 0:
            print("Quantity cannot be negative")
            return
        self.inventory.loc[self.inventory["Title"] == title, "Quantity"] = quantity
        self.inventory.to_csv(INVENTORY_FILE, index=False)
        print("Inventory updated")
    
    def record_sale(self, title, quantity, date):
        if quantity <= 0:
            print("Invalid quantity")
            return
        if title not in self.inventory["Title"].values:
            print("Book not found")
            return

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD")
            return

        price = self.inventory.loc[self.inventory["Title"] == title, "Price"].values[0]

        if self.inventory.loc[self.inventory["Title"] == title, "Quantity"].values[0] < quantity:
            print("Not enough stock")
            return

        self.inventory.loc[self.inventory["Title"] == title, "Quantity"] -= quantity
        revenue = price * quantity

        sale = {
            "Date": date,
            "Title": title,
            "Quantity Sold": quantity,
            "Total Revenue": revenue
        }

        self.sales = pd.concat([self.sales, pd.DataFrame([sale])], ignore_index=True)
        self.inventory.to_csv(INVENTORY_FILE, index=False)
        self.sales.to_csv(SALES_FILE, index=False)
        print("Sale recorded successfully")


    def generate_report(self):
        total_revenue = self.sales["Total Revenue"].sum()
        avg_price = np.mean(self.inventory["Price"])
        best_seller = self.sales.groupby("Title")["Quantity Sold"].sum().idxmax()

        print("\nBOOKSTORE REPORT")
        print("Total Revenue:", total_revenue)
        print("Average Book Price:", avg_price)
        print("Best Selling Book:", best_seller)

    # VISUALIZATION
    def visualize(self):
        merged = pd.merge(self.sales, self.inventory, on="Title")
        merged["Date"] = pd.to_datetime(merged["Date"], errors="coerce")
        
        merged["Month"] = merged["Date"].dt.month
        
        print("1. Bar Chart\n2. Line Graph\n3. Pie Chart\n4. Heatmp")
        choice = int(input("Enter choice: "))

        # Bar Chart: Sales by Genre
        if choice == 1:
            plt.figure()
            sns.barplot(data=merged, x="Genre", y="Total Revenue")
            plt.title("Total Sales by Genre")
            plt.show()

        # Line Graph: Monthly Sales
        elif choice == 2:
            monthly = merged.groupby("Month")["Total Revenue"].sum()
            plt.figure()
            monthly.plot(marker='o')
            plt.title("Monthly Sales Trend")
            plt.xlabel("Month")
            plt.ylabel("Revenue")
            plt.show()

        # Pie Chart: Revenue Share
        elif choice == 3:
            plt.figure()
            merged.groupby("Genre")["Total Revenue"].sum().plot(kind='pie', autopct='%1.1f%%')
            plt.title("Revenue Share by Genre")
            plt.ylabel("")
            plt.show()

        # Heatmap: Price vs Quantity Sold
        elif choice == 4:
            plt.figure()
            corr = merged[["Price", "Quantity Sold"]].corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm")
            plt.title("Correlation Heatmap")
            plt.show()
        
        else:
            print("Invalid choice!")

#  MAIN MENU 
def main():
    generate_sample_data()
    store = Bookstore()

    while True:
        print("\n1. Add Book")
        print("2. Update Inventory")
        print("3. Record Sale")
        print("4. Generate Report")
        print("5. Visualize Data")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            store.add_book(
                input("Title: "),
                input("Author: "),
                input("Genre: "),
                float(input("Price: ")),
                int(input("Quantity: "))
            )
            
        elif choice == 2:
            store.update_inventory(
                input("Title: "),
                int(input("New Quantity: "))
            )
            
        elif choice == 3:
            store.record_sale(
                input("Title: "),
                int(input("Quantity Sold: ")),
                input("Date (YYYY-MM-DD): ")
            )

        elif choice == 4:
            store.generate_report()
            
        elif choice == 5:
            store.visualize()
            
        elif choice == 6:
            print("Exiting system")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

