# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента.
# 1. Добавить игру против бота.
# 2. Наделить бота "интеллектом".

from random import shuffle, randint

# CANDIES = 2021
CANDIES = 100
CANDIES_LIMIT = 28
# Максимально выигрышный алгоритм для бота.
def bot_run(candies: int) -> int: # через стрелку указывается тип возвращаемого значения функции 
    result = candies % 29         # заходит остаток конфет и мы берем процент от деления на 29
    if not result:  # если выпал ноль
        result = randint(1, 28)
    return result

# Начало игры: формирование блока игроков с помощью тернарного оператора.
players = ['human', "bot" if int(input('Play with bot 1 - yes, 0 - no')) else 'person']
shuffle(players) # 1-й игрок - человек, второй - в зависимости от условия.

active_player = players[0]
print(f'1 player - {players[0]}, 2 player - {players[1]}')

while CANDIES > 0:
    print(f'\nThere are {CANDIES} sweets in the table, you can take [1...{CANDIES_LIMIT}]')
    print(f"Player {active_player}'s move") # сообщаем чей ход.
    
    if active_player == 'bot':
        get_candies = bot_run(CANDIES)
        print(f'The bot took {get_candies} candies')
    else:
        get_candies = int(input(f'How many candies do you want {active_player}: '))
        
    # проверки
    if get_candies not in range(1, CANDIES_LIMIT + 1):
        print('Wrong move!')
    else: 
        CANDIES -= get_candies
        if CANDIES > 0:
            if 'bot' in players:
                active_player = 'human' if active_player == 'bot' else 'bot'
                active_player = 'human' if active_player == 'person' else 'person'
        else:   # active_player получает результат переключения режимов.
            print(f'The player {active_player} won!')
                