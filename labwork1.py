Student = {}
Course = {}
Marks = {}


def Input_information():
    Number_Student = int(input("Number of student in class:"))
    for i in range(Number_Student):
        Student_ID = input("Student ID:")
        Student_Name = input("Student name:")
        Student_DoB = input("Student DoB:")
        Student[Student_ID] = {'name': Student_Name, 'DoB': Student_DoB}
        Number_Course = int(input("Number of course:"))
    for i in range(Number_Course):
        Course_ID = input("Course ID: ")
        Course_Name = input("Course name: ")
        Course[Course_ID] = {'name': Course_Name}


def Input_Show_Marks():
    Course_ID = input("Enter Course ID:")
    for Student_ID in Student:
        Mark = int(input(f"Enter marks for {Student[Student_ID]['name']}: "))
        if Student_ID not in Marks:
            Marks[Student_ID] = {}
        elif Student_ID in Marks and Course_ID in Marks[Student_ID]:
            print(f"Student: {Student[Student_ID]['name']}: {Marks[Student_ID][Course_ID]}")
        Marks[Student_ID][Course_ID] = Mark


Input_information()


def Option():
    print("Select:\n","1.Enter Marks And Show Student Marks:\n","2.Student List\n","3.Course List:\n","4.Student Marks:\n")
    Choice = input("Make Choice:")
    if Choice == "1":
        Input_Show_Marks()
    elif Choice == "2":
        for Course_ID in Course:
            print(f"(courses: {Course[Course_ID]['name']})")
    elif Choice == "3":
        for Student_ID in Student:
            print(f"Student: {Student[Student_ID]['name']}")
    elif Choice == "4":
        exit()
    else:
        print("please try again")

Option()
