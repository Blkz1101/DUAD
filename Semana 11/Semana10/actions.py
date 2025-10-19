import data
from main import clear

class Student:
    def __init__(self, id_, name, section, spanish, english, social_studies, science):
        self.id = id_
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science
        self.average = (spanish + english + social_studies + science) / 4

students = {}

def subject(sub):
    while True:
        sub = input("Enter the Spanish class grade of your student: ")
        try:
            sub = float(sub)
            if not (0 <= sub <= 100):
                raise Exception
            break
        except:
            print("The input has to be a number between 0 and 100")
            input("\nPress enter to restart")
            sub = None
    return sub

def classes():
    spanish = subject(None)
    english = subject(None)
    social_studies = subject(None)
    science = subject(None)
    return spanish, english, social_studies, science

def input_students():
    clear()
    name = input("Enter the full name of the student: ")
    section = input("Enter the class section of your student: ")
    spanish, english, social_studies, science = classes()

    id_ = max(students.keys()) + 1 if students else 1
    students[id_] = Student(id_, name, section, spanish, english, social_studies, science)

    clear()
    while True:
        n = input("Do you wish to input another student? (y/n): ")
        if n == "n":
            break
        elif n == "y":
            clear()
            name = input("Enter the full name of the student: ")
            section = input("Enter the class section of your student: ")
            spanish, english, social_studies, science = classes()
            id_ = max(students.keys()) + 1
            students[id_] = Student(id_, name, section, spanish, english, social_studies, science)
        else:
            print("Error. The input has to be 'y' for yes and 'n' for no")
            input("\nPress enter to restart")

def show_students(students_list=students, show_avg=True):
    clear()
    print("Students list --------------------------------")
    for s in students_list.values():
        print(f"\n{s.name}: Section: {s.section}", end="   ")
        print(f"Spanish grade: {s.spanish}", end="   ")
        print(f"English grade: {s.english}", end="   ")
        print(f"Social Studies grade: {s.social_studies}", end="   ")
        print(f"Science grade: {s.science}", end="   ")
        if show_avg:
            print(f"Average: {s.average}", end="   ")
    input("\n\nPress enter to continue")

def show_top():
    if len(students) <= 3:
        show_students()
        return
    top_students = sorted(students.values(), key=lambda s: s.average, reverse=True)[:3]
    top_dict = {s.id: s for s in top_students}
    show_students(top_dict)

def show_average():
    clear()
    print("Students list --------------------------------")
    for s in students.values():
        print(f"\n{s.name}: Average: {s.average}", end="   ")
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