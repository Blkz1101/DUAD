import menu, os
from actions import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear()
        n = menu.show_menu()
        if n == 1:
            input_students()
        elif n == 2:
            show_students(show_avg = False)
        elif n == 3:
            show_top()
        elif n == 4:
            show_average()
        elif n == 5:
            export()
        elif n == 6:
            Import()
        else:
            print("Input error. Please select a number from 1 to 6")
            x = input("\nPress enter to restart")
            clear()

if __name__ == "__main__":
    main()