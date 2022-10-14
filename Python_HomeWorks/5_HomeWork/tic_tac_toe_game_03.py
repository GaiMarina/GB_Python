
# 3. Создайте программу для игры в ""Крестики-нолики"".


def my_tic_tac_toe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")

def check_Victory(playerpos, curplayer):
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
    [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
            return True
    return False

def check_Tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) == 9:
        return True
    return False

def single_game(cur_player):
    val = [' ' for i in range(9)]
    player_pos = {'X': [], 'O': []}
    while True:
        my_tic_tac_toe(val)
        try:
            print("Player ", cur_player, " your turn. Choose your Block : ", end="")
            chance = int(input())
        except ValueError:
            print("Invalid Input!!! Try Again")
            continue
        if chance < 1 or chance > 9:
            print("Invalid Input!!! Try Again")
            continue
        if val[chance - 1] != ' ':
            print("Oops! The Place is already occupied. Try again!!")
            continue
        val[chance - 1] = cur_player
        player_pos[cur_player].append(chance)
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'
        if check_Victory(player_pos, cur_player):
            my_tic_tac_toe(val)
            print("Congratulations! Player ", cur_player, " has won the game!")
            print("\n")
            return cur_player
        if check_Tie(player_pos):
            my_tic_tac_toe(val)
            print("Oh! Game Tied")
            print("\n")
            return 'D'


        
if __name__ == "__main__":
    print("First Player")
    First_Player = input("Specify the Name: ")
    print("\n")
    print("Second Player")
    Second_Player = input("Specify the Name: ")
    print("\n")
    cur_player = First_Player
    player_choice = {'X': "", 'O': ""}
    opt = ['X', 'O']
        
    score_board = {First_Player: 0, Second_Player: 0}
    
    def my_score_board(scoreboard, cur_player):
        print("\t--------------------------------")
        print("\t         SCORE BOARD       ")
        print("\t--------------------------------")
        list_of_players = list(score_board.keys())
        print("\t   ", list_of_players[0], "\t    ",
                score_board[list_of_players[0]])
        print("\t   ", list_of_players[1], "\t    ",
                scoreboard[list_of_players[1]])
        print("\t--------------------------------\n")
        while True:
            print(cur_player, "Will you make the choice:")
            print("Press 1 for X")
            print("Press 2 for O")
            print("Press 3 to Quit")
            try:
                the_choice = int(input())
            except ValueError:
                print("Invalid Input!!! Try Again\n")
                continue
            if the_choice == 1:
                player_choice['X'] = cur_player
                if cur_player == First_Player:
                    player_choice['O'] = Second_Player
                else:
                    player_choice['O'] = First_Player
            elif the_choice == 2:
                player_choice['O'] = cur_player
                if cur_player == First_Player:
                    player_choice['X'] = Second_Player
                else:
                    player_choice['X'] = First_Player
            elif the_choice == 3:
                print("The Final Scores")
                my_score_board(score_board)
                break
            else:
                print("Invalid Selection!! Try Again\n")
                win = single_game(opt[the_choice - 1])
        if win != 'D':
            player_won = player_choice[win]
            score_board[player_won] = score_board[player_won] + 1
        my_score_board(score_board)
        if cur_player == First_Player:
            cur_player = Second_Player
        else:
            cur_player = First_Player
            
    my_score_board(score_board, cur_player)