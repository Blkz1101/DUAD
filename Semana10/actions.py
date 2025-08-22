import data
from main import clear
students = {}

def subject(sub):
    while True:
        sub = input("Enter the Spanish class grade of your student: ")
        try: 
            sub = float(sub)
            if not(sub < 101 and sub > -1): 
                raise Exception
            break
        except:
            print("The input has to be a number between 0 and 100")
            input("\nPress enter to restart")
            sub = None
    return sub

def classes():
    spanish, english, socialStudies, science = None, None, None, None
    spanish = subject(spanish)
    english = subject(english)
    socialStudies = subject(socialStudies)
    science = subject(science)
    average = (spanish + english + socialStudies + science) / 4
    return spanish, english, socialStudies, science, average

def input_students():
    clear()
    name = input("Enter the full name of the student: ")
    section = input("Enter the class section of your student: ")
    spanish, english, socialStudies, science, average = classes()
    if students: id_ = max(students.keys()) + 1
    else: id_ = 1
    students[id_] = [name, section, spanish, english, socialStudies, science, average]
    clear()
    while True:
        n = input("Do you wish to input another student? (y/n): ")
        if n == "n":
            break
        elif n == "y":
            clear()
            name = input("Enter the full name of the student: ")
            section = input("Enter the class section of your student: ")
            spanish, english, socialStudies, science, average = classes()
            id_ = max(students.keys()) + 1
            students[id_] = [name, section, spanish, english, socialStudies, science, average]
        else:
            print("Error. The input has to be 'y' for yes and 'n' for no")
            input("\nPress enter to restart")

def show_students(students_list = students, show_avg = True):
    clear()
    print("Students list --------------------------------")
    for i in students_list.keys():
        for j in range(7):
            if j == 0:
                print(f'\n{students_list[i][j]}: ', end = "")
            elif j == 1:
                print("Section:", students_list[i][j], end = "   ")
            elif j == 2:
                print("Spanish grade:", students_list[i][j], end = "   ")
            elif j == 3:
                print("English grade:", students_list[i][j], end = "   ")
            elif j == 4:
                print("Social Studies grade:", students_list[i][j], end = "   ")
            elif j == 5:
                print("Science grade:", students_list[i][j], end = "   ")
            elif j == 6 and show_avg:
                print("Average:", students_list[i][j], end = "   ")
    input("\n\nPress enter to continue")

def show_top():
    if len(students.keys()) <= 3:
        show_students()
        return
    average = {}
    for i in students.keys():
        average[students[i][6]] = i
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
        print(f'\n{students[i][0]}: ', end = "")
        print("Average:", students[i][6], end = "   ")
    input("\n\nPress enter to continue")

def export():
    clear()
    data.Export()
    print("Data exported successfully.")
    input("\nPress enter to continue")

def Import():
    clear()
    error = data.Import()
    if not error:
        print("Data imported successfully.")
    input("\nPress enter to continue")
    