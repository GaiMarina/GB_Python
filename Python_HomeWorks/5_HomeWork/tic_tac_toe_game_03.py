
# 3. Создайте программу для игры в ""Крестики-нолики"".


def tic_tac_toe_board():

    print("\n")
    print("\t")
    print("\t{}\t{}\t{}\t".format(val[0], val[1], val[2]))
    print('\t__________________')

    print("\t")
    print("\t{}\t{}\t{}\t".format(val[3], val[4], val[5]))
    print('\t__________________')

    print("\t")

    print("\t{}\t{}\t{}\t".format(val[6], val[7], val[8]))
    print("\t")
    print("\n")


def take_a_turn(sign):
    player = first_player if sign == 'X' else second_player
    while True:
        one_turn = input(
            f"Player {player}'s turn! Choose the position for {sign} from 1 to 9: ")
        if one_turn.isdigit and int(one_turn) in range(1, 10):
            one_turn = int(one_turn)
            player_pos = val[one_turn - 1]
            if player_pos not in (chr(10060), chr(11093)):
                val[one_turn - 1] = chr(10060) if sign == 'X' else chr(11093)
                break
            else:
                print(
                    f"Oops! {chr(129322)} The place is already occupied. Try again!!!")
        else:
            print(f"Invalid input! Try again!")


def check_if_victory():

    win_line = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for x in win_line:
        if val[x[0]] == val[x[1]] == val[x[2]]:
            return val[x[0]]
    return []


if __name__ == "__main__": 
    global val
    val = list(map(str, range(1, 10)))
    global first_player
    global second_player
    first_player = input("The first player, enter your name: ")
    second_player = input("The second player, enter your name: ")
    print("\n")
    counter = 0
    tic_tac_toe_board()
    while True:
        take_a_turn('0') if counter % 2 else take_a_turn('X')
        tic_tac_toe_board()

        if counter > 3:
            if check_if_victory():
                print(
                    f"{check_if_victory()} - Congratulations! You're the winner!!! {chr(127881)}{chr(129395)}{chr(127881)}")
                break
        if counter == 8:
            print(f'The game is tied {chr(129335)}')
            break
        counter += 1
