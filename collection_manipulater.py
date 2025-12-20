students = []

while True:
    print("Wlecome to the Student Data Organizer!\n")
    print("Select to the option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Sudject Offered")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("Enter student details:")
            sid = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age:"))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects_str = input("Subjects (comma-seprated): ")
            
            subjects = {s.strip() for s in subjects_str.split(",") if s.strip()}
            
            id_dob = (sid, dob)
            
            exists = False
            for s in students:
                if s["id_dob"][0] == sid:
                    exists = True
                    break
            if exists:
                print("Student is already exists. Not added.")
            else:
                student = {
                    "id_dob": id_dob,
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "subjects": subjects
                }
                students.append(student)
                print("\nStudent add Successfully\n")
                
        case 2:
            if not students:
                print("No Student Display\n")
            else:
                print("\n--- Display All Student ---\n")
                for s in students:
                    sid, dob = s["id_dob"]
                    subjects_str = ", ".join(sorted(s["subjects"]))
                    print(f"Student ID: {sid} | Name: {name} | Age: {age} | Grade: {grade} | Subject: {subjects_str}")
                    
        case 3:
            if not subjects:
                print("No student to update\n")
            else:
                sid = int(input("Enter the student id to update: "))
                index = None
                for i in range(len(students)):
                    if students[i]["id_dob"][0] == sid:
                        index = i
                        break
                
                if index is None:
                    print("Student not Found.")
                else:
                    s = students[index]
                    print("Leave field blank to keep current value.")
                    new_age = input(f"Age ({s['age']}): ").strip()
                    new_grade = input(f"Grade ({s['grade']}): ").strip()
                    new_subjects = input("Subjects (comma-separated, blank to keep same): ").strip()

                    if new_age:
                        s["age"] = new_age,
                    if new_grade:
                        s["grade"] = grade,
                    if new_subjects:
                        s["subjects"] = {x.strip() for x in new_subjects.split(",") if x.strip()}
                    
                    print("Student Updated.\n")
                    
        case 4:
            if not students:
                print("Student not deleted.\n")
            else:
                sid = int(input("Enter the student id to delete."))
                index = None
                for i in range(len(students)):
                    if students[i]["id_dob"][0] == sid:
                        index = i
                        break
                
                if index is None:
                    print("Student not Found.")
                else:
                    del students[index]
                    print("Student deleted successfully.\n")
                    
        case 5:
            all_subject = set()
            for s in students:
                all_subject.update(s["subjects"])
                
            if not all_subject:
                print("No subject display")
            
            else:
                print("\nSubjetc Offered:")
                for sub in sorted(all_subject):
                    print("-", sub)

        case 6:
            print("\nThank you for using the Student Data Organizer!")
            exit()
            
        case _:
            print("Invalied choice...")