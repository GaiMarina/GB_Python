from calculations import calculation
from calc_logging import read_log


def menu():
    flag = True
    while flag: 
        print("Приветствуем Вас в программе Калькулятор")
        while True:
            print("1 - Выполнить вычисление")
            print("2 - Посмотреть лог")
            print("3 - Выход")
            choice = input()
            if choice not in ["1", "2", "3"]:
                print("Выбран неверный пункт меню")
                continue
            if choice == "1": 
                calculation()
                break
            elif choice == "2":
                read_log()
                break
            else: 
                flag = False
                break


if __name__ == "__main__":
    menu()
