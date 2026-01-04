from datetime import datetime
import sys

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename
        self.entries = []
        self.load_entries()
        
    def load_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    self.entries = content.split("\n\n")
                else:
                    self.entries = []
        except FileNotFoundError:
            print(f"Note: The journal file '{self.filename}' does not exist. Please add a new entry.")

            
    def save_entries(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("\n\n".join(self.entries))
        except Exception as e:
            print("Error saving file: ", e)
            
    def add_entry(self, entry):
        if not entry.strip():
            print("\nEntry cannot be empty\n")
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_entry = f"[{timestamp}]\n{entry}"
        self.entries.append(full_entry)
        self.save_entries()
        print("\nEntry added successfully!\n")
        
    def view_all_entries(self):
        if self.entries:
            print("\nYour Journal Entries:")
            print("-" * 32)
            for entry in self.entries:
                print(entry,"\n")

        else:
            print("\nNo entries found. Start by adding a new entry!\n")
            
    def search_entries(self, keyword):
        if not keyword.strip():
            print("\nKeyword cannot be empty.\n")
            return
        matches = [entry for entry in self.entries if keyword.lower() in entry.lower()]

        if matches:
            print("\nMatching Entries")
            print("-" * 32)
            
            for match in matches:
                print(match,"\n")
        else:
            print(f"\nNo entries were found for the keyword: {keyword}\n")
            
    def delete_all_entries(self):
        if not self.entries:
            print("\nNo entries to delete\n")
            return
        confirm = input("\nAre you sure you want to delete all entries? (Yes/No): ").strip().lower()
        if confirm in ['yes', 'y']:
            self.entries = []
            self.save_entries()
            print("\nAll journal entries have been deleted.\n")
        else:
            print("Delete operation cancelled.")
            
def print_menu():
    print("Please select an option:\n")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search All Entries")
    print("4. Delete All Entries")
    print("5. Exit\n")

def main():
    print("Welcome to Personal Journal Manager!")
    journal = JournalManager()
    while True:
        print_menu()
        
        choice = input("User Input:\n").strip()
        if choice == "1":
            entry = input("\nEnter your journal entry: \n").strip()
            journal.add_entry(entry)
            
        elif choice == "2":
            journal.view_all_entries()
            
        elif choice == "3":
            keyword = input("\nEnter keyword to search: ").strip()
            journal.search_entries(keyword)

        elif choice == "4":
            journal.delete_all_entries()

        elif choice == "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!\n")
            sys.exit(0)
            
        else:
            print("\nInvalid option. Please select a valid option from the menu\n")

if __name__ == "__main__":
    main()
