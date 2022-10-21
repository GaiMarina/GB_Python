from info_input import data_input
from data_logger import log_input, log_import
from format_saving import html_exp, csv_to_excel
from searching import search


def main_menu():
    print("Now you've opened the phone book.")
    while True:
        print()
        print('Choose the number of operation to do: ')
        print('1 - to make a new record: ')
        print('2 - to download and read the phone book: ')
        print('3 - to export the phone book to the following formats: ')
        print('4 - to search the necessary record: ')
        print('5 - to exit.')
        ch = input()
        if ch not in ["1", "2", "3", "4", "5"]:
            print("The wrong input. Try again!")
            continue
        elif ch == '1':
            ent = data_input()
            log_input(ent)
            continue
        elif ch == '2':
            print()
            log_import()
            continue
        elif ch == '3':
            print('Input 1 to export the phone book to .html format.')
            print('Input 2 to export the phone book to .xlsx.')
            f_ch = input()
            if f_ch not in ["1", "2"]:
                print("The wrong input. Try again!")
                continue
            elif f_ch == '1':
                html_exp()
                continue
            elif f_ch == '2':
                csv_to_excel()
                continue
        elif ch == '4':
            search()
            continue
        elif ch == '5':
            print()
            print('Thanks for using the phone book.')
            break


if __name__ == "__main__":
    main_menu()
