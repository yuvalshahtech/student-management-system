def delete_student(students):
    deleted=False
    delete_name=input("Enter name to delete: ").title()
    delete_name=validate_non_empty(delete_name)
    for index,item in enumerate(students):
        if item["Name"]==delete_name:
            confirm = input("Are you sure you want to delete? (yes/no): ").lower()
            if confirm == "yes":
                del students[index]
                deleted=True
                break
    if deleted==False:
        print("No such student exists.")
def update_student(students):
    updated=False
    update_name=input("Enter name to update marks: ").title()
    update_name=validate_non_empty(update_name)
    for index,item in enumerate(students):
        if item["Name"]==update_name:
            x=int(input("Enter new marks for the student: "))
            students[index]["Marks"]=validate_marks(x)
            students[index]["GPA"]=calculate_gpa(x)
            updated=True
            break
    if updated==False:
        print("No such student exists.")
def search_student(students):
    found=False
    search_name=input("Enter name to search: ").title()
    search_name=validate_non_empty(search_name)
    for index,item in enumerate(students):
        if item["Name"]==search_name:
            for key,value in item.items():
                print(f"{key}: {value}")
            print("---------------------")
            found=True
            break
    if found==False:
        print("No such student exists.")
def view_all(students):
    for index,item in enumerate(students):
        print(f"------Student {index+1}------")
        for key,value in item.items():
            print(f"{key}: {value}")
        print("---------------------")
def calculate_gpa(marks):
    gpa=marks/10
    return gpa
def validate_marks(marks):
    while True:
        if marks<0 or marks>100:
            marks=int(input("Please enter valid marks: "))
        else:
            return marks
def validate_age(age):
    while True:
        if age<0:
            age=int(input("Please enter valid age: "))
        else:
            return age
def validate_non_empty(input_name):
    while input_name.strip() == "":
        input_name = input("Name cannot be empty. Please enter again: ").title()
    return input_name.title()
def add_student(students):
    name=input("Enter your name: ").title()
    name=validate_non_empty(name)
    age=int(input("Enter your age: "))
    age=validate_age(age)
    subject=input("Enter subject name: ").title().strip()
    subject=validate_non_empty(subject)
    marks=int(input(f"Enter your marks in {subject}: "))
    marks=validate_marks(marks)
    gpa=calculate_gpa(marks)
    new_student={
    "Name": name,
    "Age": age,
    "Subject": subject,
    "Marks": marks,
    "GPA": gpa
    }
    students.append(new_student)
def validate_choice(choice,max_choice):
    while True:
        if choice<1 or choice>max_choice:
            choice=int(input("You accidentally entered an invalid choice. Please try again: "))
        else:
            return choice
def display():
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")
def main():
    students=[]
    max_choice=6
    while True:
        display()
        choice=int(input("Enter your choice: "))
        choice=validate_choice(choice,max_choice)
        if choice==1:
            add_student(students)
        elif choice==2:
            if len(students)==0:
                print("Database is Empty")
            else:
                view_all(students)
        elif choice==3:
            search_student(students)
        elif choice==4:
            update_student(students)
        elif choice==5:
            delete_student(students)
        else:
            print("Thank You for using Student Manager System")
            break

if __name__=="__main__":
    main()
