class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        
class Employee(Person):
    def __init__(self, name, age, employee_id = None, salary = 0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary
        
    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id
        
    def get_employee_id(self):
        return self.__employee_id
    
    def set_salary(self, salary):
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary
    
    @classmethod
    def from_name_age(cls, name, age):
        return cls(name, age)
    
    @classmethod
    def from_full_data(cls, name, age, emp_id, salary):
        return cls(name, age, emp_id, salary)
    
    def display(self):
        super().display()
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: {self.__salary}")
        
    def __del__(self):
        return 0
        # print("Exiting the system. All resources have been freed")

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department
        
    def display(self):
        super().display()
        print(f"Department: {self.department}")

def create_person():
    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))
    return Person(name, age)

def create_employee():
    name = input("\nEnter name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    return Employee.from_full_data(name, age, emp_id, salary)

def create_manager():
    name = input("\nEnter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    dept = input("Enter Department: ")
    return Manager(name, age, emp_id, salary, dept)

def show_details(person, employee, manager):
    print("Choose details to show")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    choice = int(input("\nEnter choose: "))
    
    if choice == 1:
        if person:
            print("\nPerson Details:")
            person.display()
        else:
            print("\nPerson not created.")
        
    elif choice == 2:
        if employee:
            print("\nEmployee Details:")
            employee.display()
        else:
            print("\nEmployee not created.")
        
    elif choice == 3:
        if manager:
            print("\nManager Deatils:")
            manager.display()
        else:
            print("\nManager not created.")
    
    else:
        print("No object created for the type\n")
        
        
def main():
    person = None
    employee = None
    manager = None
    
    print("--- Python OOP Project: Employee Management System ---\n")

    while True:
        print("Choose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Deatils")
        print("5. Exit")

        ch = int(input("\nEnter choice: "))
        
        if ch == 1:
            person = create_person()
            print(f"\nPerson created with name: {person.name} and age: {person.age}")
            
        elif ch == 2:
            employee = create_employee()
            print(f"\nEmployee created with name: {employee.name}, age: {employee.age}, ID: {employee.get_employee_id()}, salary: {employee.get_salary():.1f}\n")
            
        elif ch == 3:
            manager = create_manager()
            print(f"\nManager created with name: {manager.name}, age: {manager.age}, ID: {manager.get_employee_id()}, salary: {manager.get_salary()}, and department: {manager.department}\n")
            
        elif ch == 4:
            show_details(person, employee, manager)
            
        elif ch == 5:
            print("\nExiting the system. All resources have been freed")
            print("\nGoodbye!")
            break
        
        else:
            print("Invalied Choice")
        
        print("\n--- Choose another operation ---\n")

if __name__ == "__main__":
    main()