import math
import pickle
import random
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1
PLAYER2 = 1


EMPTY = " "
PLAYER_PIECE = "X"
AI_PIECE = "O"
PLAYER1_PIECE = "O"
WINDOW_LENGTH = 4


def create_board():
    board = np.array([[" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "], [" "," "," "," "," "," "," "]])
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == " "


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == " ":
            return r

def check_for_full_column(board,col):
    r = 6
    if board[5][col] != " ":
        return True
    else:
        False


def print_board(board):

    top = '   1   2   3   4   5   6   7'
    print("    #######################\n"
          "    ###### CONNECT 4 ######\n"
          "    #######################\n"
          "                             ")
    print(np.flip(board, 0))
    print(top)


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0

    ## Score center column
    center_array = [str(i) for i in list(board[:, COLUMN_COUNT // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [str(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [str(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score posiive sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score

def check_if_draw(board):
    for z in range(ROW_COUNT):
        for s in range(COLUMN_COUNT):
            if board[5][0] and board[5][1] and board[5][2] and board[5][3] and board[5][4] and board[5][5] and board[5][6] != " ":
                return True
            else:
                return False

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == " "


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def pick_best_move(board, piece):
    valid_locations = get_valid_locations(board)
    best_score = 0
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, board)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col


def main():
    Set0 = {'1', '2', '3', '4', '5', '6', '7'}
    game_over = False
    turn = 0
    print("Game mode player vs ai = 1\n"
          "Game mode player vs player = 2\n"
          "Game mode ai vs ai = 3")    #Todo
    game_mode = int(input("Please choose a game mode: "))
    print("To load up an old game enter \"y\" if not enter \"n\" \n"
          "This will load up the game that you last saved using the command \"close\"")
    old_game = str(input("Load old game: "))
    if old_game == "y":
        with open('/usr/saveddata/savefile.dat', 'rb') as f:
            board= pickle.load(f)
            print_board(board)
    elif old_game == "n":
        board = create_board()
        print_board(board)
    if game_mode == 3:
        turn = random.randint(PLAYER, AI)
        if turn == 0:
            print("AI 1")
        elif turn == 1:
            print("AI 2")
    while not game_over:
        if game_mode == 1:
            if check_if_draw(board):
                print("Its a draw")
                game_over = True
            else:
                if turn == PLAYER:
                    col = str(input("Player " + PLAYER_PIECE +" enter your move: "))
                    if col in Set0:
                        col = int(col) - 1
                        if check_for_full_column(board,col):
                            print("Column full")
                        else:
                            if is_valid_location(board, col):
                                row = get_next_open_row(board, col)
                                drop_piece(board, row, col, PLAYER_PIECE)

                                if winning_move(board, PLAYER_PIECE):
                                    print("X wins!")
                                    game_over = True
                                    break
                                turn += 1
                                turn = turn % 2
                    elif col == "close":
                        with open('/usr/saveddata/savefile.dat', 'wb') as f:
                            pickle.dump(board, f, protocol=2)
                        print("Game saved")
                        exit()
                    else:
                        print("Please enter a number between 1 and 7 or close to end the game")
                if turn == AI and not game_over:
                    col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, AI_PIECE)

                        if winning_move(board, AI_PIECE):
                            print_board(board)
                            print("AI wins!")
                            game_over = True
                            break

                        print_board(board)

                        turn += 1
                        turn = turn % 2

        elif game_mode == 2:
            if check_if_draw(board):
                print("Its a draw")
                game_over = True
            else:
                if turn == PLAYER:
                    col = str(input("Player " + PLAYER_PIECE +" enter your move: "))
                    if col in Set0:
                        col = int(col) - 1
                        if check_for_full_column(board,col):
                            print("Column full")
                        else:

                            if is_valid_location(board, col):
                                row = get_next_open_row(board, col)
                                drop_piece(board, row, col, PLAYER_PIECE)

                                if winning_move(board, PLAYER_PIECE):
                                    print_board(board)
                                    print("X wins!")
                                    game_over = True
                                    break
                            turn += 1
                            turn = turn % 2
                            print_board(board)
                    elif col == "close":
                        with open('/usr/saveddata/savefile.dat', 'wb') as f:
                            pickle.dump(board, f, protocol=2)
                        print("Game saved")
                        exit()
                    else:
                        print("Please enter a number between 1 to 7 or close to end the game")

                if turn == PLAYER2:
                    col = str(input("Player " + PLAYER1_PIECE +" enter your move: "))
                    if col in Set0:
                        col = int(col) - 1
                        if check_for_full_column(board,col):
                            print("Collomn full")
                        else:
                            if is_valid_location(board, col):
                                row = get_next_open_row(board, col)
                                drop_piece(board, row, col, PLAYER1_PIECE)

                                if winning_move(board, PLAYER1_PIECE):
                                    print_board(board)
                                    print("O wins!")
                                    game_over = True
                                    break
                            turn += 1
                            turn = turn % 2
                            print_board(board)
                    elif col == "close":
                        with open('/usr/saveddata/savefile.dat', 'wb') as f:
                            pickle.dump(board, f, protocol=2)
                        print("Game saved")
                        exit()
                    else:
                        print("Please enter a number between 1 to 7 or close to end the game")

        elif game_mode == 3:
            if check_if_draw(board):
                print("Its a draw")
                game_over = True
            else:
                if turn == PLAYER:
                    col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)

                        if winning_move(board, PLAYER_PIECE):
                            print_board(board)
                            print("AI 1 wins!")
                            game_over = True
                            break
                        print_board(board)
                        turn += 1
                        turn = turn % 2
                if turn == AI and not game_over:
                    col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, AI_PIECE)

                        if winning_move(board, AI_PIECE):
                            print_board(board)
                            print("AI 2 wins!")
                            game_over = True
                            break

                        print_board(board)

                        turn += 1
                        turn = turn % 2


if __name__ == '__main__':
    main()
