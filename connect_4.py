
class Stack:
    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return

    def peek(self):
        return self._list[-1]


def initBoard():
    rows = ['a', 'b', 'c', 'd', 'e', 'f']
    board = []
    for i in range(0, len(rows)):
        board.append([' '] * 7)

    return board


def initStacks():
    S = [Stack(), Stack(), Stack(),
         Stack(), Stack(), Stack(), Stack()]
    return S


def printBoard(board):
    print("###############################\n"
          "######### CONNECT 4 ###########\n"
          "###############################")

    rows = ['a', 'b', 'c', 'd', 'e', 'f']
    top = '    1   2   3   4   5   6   7   '
    row = [[n] for n in range(0, 7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-' * (len(top) - 3))
    for j in range(0, len(rows)):
        for i in range(1, 8):
            row[j][0] = row[j][0] + str(board[j][i - 1]) + ' | '
        print(row[j][0])
        print('  ' + '-' * ((len(row[j][0]) - 3)))
    print(top)
    print('')


def move(piece, board, Stacks, computer):
    Set0 = {'1', '2', '3', '4', '5', '6', '7'}
    if piece != computer:
        pos = str(input(piece + ' move: '))
        if (pos in Set0) == False:
            print('Input must be integer between 1 and 7')
            move(piece, board, Stacks, computer)
        else:
            pos = int(pos)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6 - len(Stacks[pos - 1])][pos - 1] = \
                    Stacks[pos - 1].peek()
            else:
                print('Column full, try again...')
                move(piece, board, Stacks, computer)
    elif piece == computer:
        pos = str(input(piece + ' move: '))
        if (pos in Set0) == False:
            print('Input must be integer between 1 and 7')
            move(piece, board, Stacks, computer)
        else:
            pos = int(pos)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6 - len(Stacks[pos - 1])][pos - 1] = \
                    Stacks[pos - 1].peek()
            else:
                print('Column full, try again...')
                move(piece, board, Stacks, computer)

    return board, Stacks

def checkWin(S, board):
    game = False
    # Horizontal
    for z in range(0, 6):
        for s in range(3, 7):
            if (board[z][s] == board[z][s - 1] == board[z][s - 2] == board[z][s - 3] == S):
                game = True
            else:
                continue
    # Vertical
    for s in range(0, 7):
        for z in range(3, 6):
            if (board[z][s] == board[z - 1][s] == board[z - 2][s] == board[z - 3][s] == S):
                game = True
            else:
                continue
    # Diagonal
    for s in range(0, 4):
        for z in range(0, 3):
            if (board[z][s] == board[z + 1][s + 1] == board[z + 2][s + 2] == board[z + 3][s + 3] == S or
                    board[z + 3][s] == board[z + 2][s + 1] == board[z + 1][s + 2] == board[z][s + 3] == S):
                game = True
            else:
                continue
    if game == True:
        print(S + ' wins!')
    return game


def main():
    player1 = str(input('X or O: '))
    if player1 != 'X' and player1 != 'O':
        player1 = str(input('X or O: '))
    if player1 == 'X':
        computer1 = 'O'
    else:
        computer1 = 'X'
    board = initBoard()
    Stacks = initStacks()
    printBoard(board)
    game = False
    while game == False:
        board, Stacks = move('X', board, Stacks, computer1)
        printBoard(board)
        game = checkWin('X', board)
        if game == True:
            break

        board, Stacks = move('O', board, Stacks, computer1)
        printBoard(board)
        game = checkWin('O', board)
        if game == True:
            break
    print('Good game')

if __name__ == '__main__':
    main()
