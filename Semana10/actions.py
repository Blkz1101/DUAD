import data
from main import clear
students = {}

def classes():
    spanish, english, socialStudies, science = None, None, None, None
    while True:
        if spanish == None:
            spanish = input("Enter the Spanish class grade of your student: ")
        elif spanish.isnumeric() and int(spanish) < 101 and int(spanish) > -1: 
            spanish = int(spanish)
            break
        else:
            print("The input has to be a number between 0 and 100")
            x = input("\nPress enter to restart")
            clear()
            spanish = None
    while True:
        if english == None:
            english = input("Enter the English class grade of your student: ")
        elif english.isnumeric() and int(english) < 101 and int(english) > -1: 
            english = int(english)
            break
        else:
            print("The input has to be a number between 0 and 100")
            x = input("\nPress enter to restart")
            clear()
            english = None
    while True:
        if socialStudies == None:
            socialStudies = input("Enter the Social Studies class grade of your student: ")
        elif socialStudies.isnumeric() and int(socialStudies) < 101 and int(socialStudies) > -1: 
            socialStudies = int(socialStudies)
            break
        else:
            print("The input has to be a number between 0 and 100")
            x = input("\nPress enter to restart")
            clear()
            socialStudies = None
    while True:
        if science == None:
            science = input("Enter the Science class grade of your student: ")
        elif science.isnumeric() and int(science) < 101 and int(science) > -1: 
            science = int(science)
            break
        else:
            print("The input has to be a number between 0 and 100")
            x = input("\nPress enter to restart")
            clear()
            science = None
    average = (spanish + english + socialStudies + science) / 4
    return spanish, english, socialStudies, science, average

def input_students():
    clear()
    name = input("Enter the full name of the student: ")
    section = input("Enter the class section of your student: ")
    spanish, english, socialStudies, science, average = classes()
    students[name] = [section, spanish, english, socialStudies, science, average]
    clear()
    while True:
        n = input("Do you wish to input another student? (y/n): ")
        if n == "n":
            clear()
            break
        elif n == "y":
            clear()
            name = input("Enter the full name of the student: ")
            section = input("Enter the class section of your student: ")
            spanish, english, socialStudies, science, average = classes()
            students[name] = [section, spanish, english, socialStudies, science, average]
        else:
            print("Error. The input has to be 'y' for yes and 'n' for no")
            x = input("\nPress enter to restart")
            clear()

def show_students(students_list = students):
    clear()
    print("Students list --------------------------------")
    for i in students_list.keys():
        print("\n", i, end = ": ")
        for j in range(6):
            if j == 0:
                print("Section:", students_list[i][j], end = "   ")
            elif j == 1:
                print("Spanish grade:", students_list[i][j], end = "   ")
            elif j == 2:
                print("English grade:", students_list[i][j], end = "   ")
            elif j == 3:
                print("Social Studies grade:", students_list[i][j], end = "   ")
            elif j == 4:
                print("Science grade:", students_list[i][j], end = "   ")
            elif j == 4 and students_list == students:
                print("Average:", students_list[i][j], end = "   ")
    x = input("\n\nPress enter to continue")
    clear()

def show_top():
    if len(students.keys()) <= 3:
        show_students()
        return
    clear()
    average = {}
    for i in students.keys():
        average[students[i][5]] = i
    averageExtra = sorted(average.keys(), reverse = True)
    averageExtra = averageExtra[0], averageExtra[1], averageExtra[2]
    students_list = {}
    for i in range(3):
        students_list[average[averageExtra[i]]] = students[average[averageExtra[i]]]
    show_students(students_list)

def show_average():
    clear()
    print("Students list --------------------------------")
    for i in students.keys():
        print("\n", i, end = ": ")
        print("Average:", students[i][5], end = "   ")
    x = input("\n\nPress enter to continue")
    clear()

def export():
    clear()
    data.Export()
    print("Data exported successfully.")
    x = input("\nPress enter to continue")
    clear()

def Import():
    clear()
    error = data.Import()
    if not error:
        print("Data imported successfully.")
    x = input("\nPress enter to continue")
    clear()
    