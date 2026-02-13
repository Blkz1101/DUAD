def show_menu():
    print('''- - - - - - - - - - - - - - - - - - Menu - - - - - - - - - - - - - - - - - -
Please select one of the following options:

1. Input students information
2. See students information
3. See the top three students (Based on average score)
4. See students average score
5. Export data to a CSV file
6. Import data from a CSV file
''')
    n = input()
    try: return (int(n))
    except ValueError: return