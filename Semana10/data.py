import actions, csv

def Export():
    headers = ['id', 'fullname', 'section', 'spanish', 'english', 'socialStudies', 'science', 'average']
    with open('Semana10/students.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)

        for id, values in actions.students.items():
            csv_writer.writerow([id] + values)
        
def Import():
    students = {}
    try:
        r = input("Enter the file path inside of Semana10 or press enter to use default (Remember the .csv): ")
        if r == "": r = 'students.csv'
        with open(f'Semana10/{r}', mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                id = row[0]  
                values = [row[1]] + [float(i) for i in row[2:]]   
                students[id] = values

            actions.students.clear()
            actions.students.update(students)
    except FileNotFoundError:
        print("Error. Exported file not found")
        return True