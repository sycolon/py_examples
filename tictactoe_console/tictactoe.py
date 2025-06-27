import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = "X"
winner = None
gameRunning = True

# printing the game board
def printBoard(board):
    for i,el in enumerate(board):
        print(el + " | ",end="")
        if i == 2:
            print()
            print("-"*11)
        if  i == 5:
            print()
            print("-"*11)
        if  i == 8:
            print()
            print("-"*11)

# take player input

def PlayerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer # X or O
    else:
        print("A player is already in that position!")

# check for win or tie
def checkHoriz(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3]!= "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6]!= "-":
        winner = board[6]
        return True

def checkVerti(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1]!= "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2]!= "-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2]!= "-":
        winner = board[2]
        return True

def checkWin():
    global gameRunning
    if checkDiag(board)  or checkHoriz(board)  or checkVerti(board) :
        print(f"The winner is {winner}")
        printBoard(board)
        gameRunning = False
        return 

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie")
        gameRunning = False

# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer ="O"
    else :
        currentPlayer = "X"

# Computer playing
def cpuPlayer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] ="O"
            switchPlayer()
# check for with or tie again
# MainApp
while gameRunning:
    printBoard(board)
    PlayerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    cpuPlayer(board)
    checkWin()
    checkTie(board)
