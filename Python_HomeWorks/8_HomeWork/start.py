from input import head_line_input, user_input, data_export
from data_watch import csv_to_excel, database_import
from database_operations import user_search

def main_menu():
    print("Now you've opened the database.")
    while True:
        print()
        print('Choose the number of operation to do: ')
        print('1 - to add the new column: ')
        print('2 - to input the new user information: ')
        print('3 - to download and see the database: ')
        print('4 - to export the database to .xlsx format: ')
        print('5 - to search the necessary user information: ')
        print('6 - to save all the changes and exit.')
        ch = int(input())
        if ch not in range(1, 7):
            print("The wrong input. Try again!")
            continue
        elif ch == 1:
            head_line_input()
            continue
        elif ch == 2:
            print()
            user_input()
            data_export()
            continue
        elif ch == 3:
            database_import()
            continue
        elif ch == 4:
            csv_to_excel()
            continue
        elif ch == 5:
            user_search()
        elif ch == 6:
            print()
            print('Thanks for using the database!')
            break


if __name__ == "__main__":
    main_menu()
