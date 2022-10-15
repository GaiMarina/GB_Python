
# 2. Создайте программу для игры с конфетами человек против человека.
#    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#    Все конфеты оппонента достаются сделавшему последний ход. 
#    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#    a) Добавьте игру против бота
#    b) Подумайте как наделить бота ""интеллектом""


from random import randint

def move_making(mode, name, candies_left):
    q = 0
    while not q:
        if mode == 1:
            q = input(f'{name}! Enter the number of candies to take from 1 to 28: ') 
            if q.isdigit and int(q) in range(1, 29):
                q = int(q)
            else:
                q = 0
                print(f"Invalid input! Try again!")
        elif mode == 2:
            q = randint(1, 29)
        else:
            q = candies_left // 28 - 1
            if q == 0:
                q = 1
    return q

def print_result(candies, player, cans_take):
    print(f'{cans_take} taken by the {player}')
    print(f'{candies} of the candies left.')

if __name__ == "__main__":
    game_mode_select = int(input(' 1 - human vs human\n 2 - human vs PC\n 3 - human vs IQ\n Enter your choice: '))
    first_plr = input('The first player, input your name: ')
    if game_mode_select == 1:
        second_plr = input('The second player, input your name: ')
    else:
        second_plr = 'bot'
    all_the_candies = 0
    while not all_the_candies:
        all_the_candies = input('Enter the total number of candies: ')
        if all_the_candies.isdigit:
            all_the_candies = int(all_the_candies)
        else:
            all_the_candies = 0
            print(f"Invalid input! Try again!")
            
    toss_up = randint(0, 2)
    if toss_up:
        print(f'{first_plr} makes the first move.')
    else:
        print(f'{second_plr} makes the first move.')

    while all_the_candies > 28:
        candies_taken = move_making(1 if toss_up else game_mode_select, 
                                        first_plr if toss_up else second_plr, 
                                        all_the_candies)
        all_the_candies -= candies_taken
        print_result(all_the_candies, first_plr if toss_up else second_plr, candies_taken)
        toss_up = not toss_up
    print(f'Congratulations! {first_plr if toss_up else second_plr} is a winner!')
    
