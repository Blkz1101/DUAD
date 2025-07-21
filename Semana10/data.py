import actions, csv

def Export():
    headers = ['fullname', 'section', 'spanish', 'english', 'socialStudies', 'science', 'average']
    with open('Semana10/students.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)

        for fullname, values in actions.students.items():
            csv_writer.writerow([fullname] + values)
        
def Import():
    students = {}
    try:
        with open('Semana10/students.csv', mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                fullname = row[0]  
                values = row[1:]   
                students[fullname] = values

            actions.students.clear()
            actions.students.update(students)
    except FileNotFoundError:
        print("Error. Exported file not found")
        return True