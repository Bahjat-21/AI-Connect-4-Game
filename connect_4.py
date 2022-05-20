
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
    # empty board
    rows = ['a', 'b', 'c', 'd', 'e', 'f']
    board = []
    for i in range(0, len(rows)):
        board.append([' '] * 7)

    return board  # Initialize Stacks (empty


def initStacks():
    S = [Stack(), Stack(), Stack(),
         Stack(), Stack(), Stack(), Stack()]
    return S

def printBoard(board):
    print(  "###############################\n"
            "######### CONNECT 4 ###########\n"
            "###############################")

    rows = ['a','b','c','d','e','f']
    top = '    1   2   3   4   5   6   7   '
    row = [[n] for n in range(0,7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-'*(len(top)-3))
    for j in range(0,len(rows)):
        for i in range(1,8):
            row[j][0] = row[j][0] + str(board[j][i-1]) + ' | '
        print(row[j][0])
        print('  ' + '-'*((len(row[j][0])-3)))
    print(top)
    print('')

def move(piece, board, Stacks, player):
    Set0 = {'1','2','3','4','5','6','7'}
    pos = str(input('Your move: '))
    if (pos in Set0) == False:
        print('Input must be integer between 1 and 7')
        move(piece,board,Stacks,player)
    else:
        pos = int(pos)
        Stacks[pos-1].push(piece)
        board[6-len(Stacks[pos-1])] [pos-1] = Stacks[pos-1].peek()
        game = True
    return board, Stacks



def main():
    board = initBoard()
    Stacks = initStacks()
    printBoard(board)
    player1 = str(input('X oder O: '))
    if player1 != 'X' and player1 != 'O':
        player1 = str(input('X oder O: '))
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    game = False
    while game == False:
        board, Stacks = move('X', board, Stacks, player1)
        printBoard(board)



if __name__ == '__main__':
    main()