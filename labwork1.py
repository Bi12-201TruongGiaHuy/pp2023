stu = {} 
courses = {} 
points = {} 

def student():
    n_stu = int(input("Enter the number of students:"))
    for i in range(n_stu):
        stu_id = input("Enter stu id: ")
        stu_name = input("Enter stu name: ")
        stu_DoB = input("Enter stu DoB: ")
        stu[stu_id]= {'name': stu_name, 'DoB': stu_DoB}

def course():
    n_courses = int(input("Enter the number of the courses: "))
    for i in range(n_courses):
        courses_id = input("Enter courses id: ")
        courses_name = input("Enter courses name: ")
        courses[courses_id]= {'name': courses_name}

def pointss():
    courses_id = input("Enter the course id: ")
    if courses_id not in courses:
        print("Not found")
        return
    for stu_id in stu:
        point = int(input(f"Enter the point for {stu[stu_id]['name']}: "))
        if stu_id not in points:
            points[stu_id] = {}
        points[stu_id][courses_id] = point

def l_courses():
    for courses_id in courses:
        print(f"(courses_id: {courses[courses_id]['name']})")

def l_student():
    for stu_id in stu:
        print(f"(students_id: {stu[stu_id]['name']})")

def show_point():
    courses_id = input("Enter the courses id: ")
    if courses_id not in courses:
        print("Not found")
        return
    for stu_id in stu:
        if stu_id in points and courses_id in points[stu_id]:
            print(f"(students_id: {stu[stu_id]['name']}: {points[stu_id][courses_id]}")
        else:
            print(f"{stu[stu_id]['name']}: Not found")

student()
course()

while True:
    print("Select: ")
    print("1.Input point of a course")
    print("2.List courses")
    print("3.List Students")
    print("4.student point of the given courses")
    print("5.End")
    choice = input("Enter your choice: ")
    if choice == "1":
        pointss()
    elif choice == "2":
        l_courses()
    elif choice == "3":
        l_student()
    elif choice == "4":
        show_point()
    elif choice == "5":
        break
    else:
        print("Invalid")
