# Создайте программу для игры в ""Крестики-нолики"".

wins_coord = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def draw_board(board):
    print('-' * 12)
    for i in range(3):
        print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3])
    print('-' * 12)    

def step(player_token, board):
    while True:
        value = int(input(f'Куда поставить {player_token} ? '))
        if not (str(value) in '123456789'):
            print('Ошибочный ввод. Введите число от 1 до 9 на свободных позициях')
            continue
        if str(board[value - 1]) in 'XO':
            print('Это поле уже занято.')
            continue
        board[value - 1] = player_token
        break

def check_win(board):
    for each in wins_coord:
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1]:
            return board[each[1]-1]
    else:
        return False


def main(board):
    counter = 0
    while True:
        draw_board(board)
        if counter % 2 == 0:
            step('X', board)
        else:
            step('O', board)
        if counter > 3:
            winner = check_win(board)
            if winner:
                draw_board(board)
                print(winner, 'выиграл!')
                break
        counter += 1
        if counter > 8:
            draw_board(board)
            print('Ничья!')
            break

lst_board = list(range(1, 10))
main(lst_board)