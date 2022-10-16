# 3. Программа для игры в "Крестики-нолики".format
#    Поле 3x3ю Игрок - игрок, без бота.
   
from curses.ascii import isdigit


board = list(map(str, range(1, 10)))


def draw_board():   # Рисуем поле.
    print('-' * 20) # написали подчеркивание
    for i in range(3):
        for k in range(3): 
            print(f'{board[k + i * 3]:^5}', end=' ') # Формула вывода 3 раза.
        print(f'\n{"-" * 20}')      # ^ - выравнивание по центру.
    print()
    
    
def place_sign(token):      # Размещение X, 0. Функция выбирает и ставит элемент на поле.
    global board
    while True:     # Когда нужно прерываться в середине через break
        answer = input(f'Enter a number from 1 to 9.\nSelect a position {token}: ')
        if answer.isdigit and int(answer) in range(1, 10):
            answer = int(answer)
            pos = board[answer - 1]
            if pos not in (chr(10060), chr(11093)):
                board[answer - 1] = chr(10060) if token == 'X' else chr(11093) # записываем в ячейку знак.
                break   # тернарный оператор/условное выражение: == истина, делаем то, что слева, если
            else:       # ложно, то то, что после else
                print(f'This cell is already occupied{chr(9995)}{chr(129292)}')
        else:
            print(f'Incorrect input{chr(9940)}. Are you sure you entered a correct number?')
            
def check_win():   # Проверка на выигрыш.
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n # возвращает либо крестик, либо нолик, если нет одинаковых значков в линию,
                            # возвращает пустой список n

def main():
    counter = 0 # счетчик ходов.
    draw_board()
    while True: # крутимся в бесконечном цикле, выход только если ничья или выигрыш.
        place_sign('0') if counter % 2 else place_sign('X') # переключение режима активного игрока.
        draw_board()
        
        if counter > 3:
            if check_win():
                print(f'{check_win()} - WIN{chr(127942)}{chr(127881)}')
                break
        if counter == 8:
            print(f'Drawn game {chr(129318)}{chr(129309)}!')
            break
        counter += 1
        
main()