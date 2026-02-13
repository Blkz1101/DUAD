import actions, csv
from actions import Student

def Export():
    headers = ['id', 'fullname', 'section', 'spanish', 'english', 'socialStudies', 'science', 'average']
    with open('Semana10/students.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)

        for s in actions.students.values():
            csv_writer.writerow([
                s.id,
                s.name,
                s.section,
                s.spanish,
                s.english,
                s.social_studies,
                s.science,
                s.average
            ])

def Import():
    try:
        r = input("Enter the file path inside of Semana10 or press enter to use default (Remember the .csv): ")
        if r == "":
            r = 'students.csv'

        with open(f'Semana10/{r}', mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # saltar encabezado

            actions.students.clear()

            for row in csv_reader:
                id_ = int(row[0])
                name = row[1]
                section = row[2]
                spanish = float(row[3])
                english = float(row[4])
                social_studies = float(row[5])
                science = float(row[6])
                # el promedio se calcula dentro de Student
                actions.students[id_] = Student(id_, name, section, spanish, english, social_studies, science)

        print("Data imported successfully.")
        return False

    except FileNotFoundError:
        print("Error. Exported file not found")
        return True