import tkinter as tk
from tkinter import messagebox
import time
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

board = []
custom_font = ("Arial",48)
currentPlayer = "X"
winner = None
tieGameBoard = []

def play(btn):
    if btn.cget('text') == "-":
        btn.config(text=currentPlayer)
        if currentPlayer == "O":
            btn.config(style="info.TButton")
            
        elif currentPlayer == "X":
            btn.config(style="warning.TButton")
        
    else:
        messagebox.showinfo("Warning","Move not allowed is already used")
        switchPlayer()


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer ="O"
    else :
        currentPlayer = "X"

def play_and_switch(btn):
    #print(board)
    play(btn)
    checkWin()
    checkTie(board)
    switchPlayer()

#################################################

def checkHoriz(board):
    global winner
    if board[0].cget('text') == board[1].cget('text') == board[2].cget('text') and board[0].cget('text')!= "-":
        winner = board[0].cget('text')
        return True
    elif board[3].cget('text') == board[4].cget('text') == board[5].cget('text') and board[3].cget('text')!= "-":
        winner = board[3].cget('text')
        return True
    elif board[6].cget('text') == board[7].cget('text') == board[8].cget('text') and board[6].cget('text')!= "-":
        winner = board[6].cget('text')
        return True

def checkVerti(board):
    global winner
    if board[0].cget('text') == board[3].cget('text') == board[6].cget('text') and board[0].cget('text')!= "-":
        winner = board[0].cget('text')
        return True
    elif board[1].cget('text') == board[4].cget('text') == board[7].cget('text') and board[1].cget('text')!= "-":
        winner = board[1].cget('text')
        return True
    elif board[2].cget('text') == board[5].cget('text') == board[8].cget('text') and board[2].cget('text')!= "-":
        winner = board[2].cget('text')
        return True

def checkDiag(board):
    global winner
    if board[0].cget('text') == board[4].cget('text') == board[8].cget('text') and board[0].cget('text')!= "-":
        winner = board[0].cget('text')
        return True
    elif board[2].cget('text') == board[4].cget('text') == board[6].cget('text') and board[2].cget('text')!= "-":
        winner = board[2].cget('text')
        return True


def checkTie(board):
    #global gameRunning
    global tieGameBoard
    tieGameBoard= []
    for i in range(9):
        tieGameBoard.append(board[i].cget('text'))
    if "-" not in tieGameBoard and winner == None:
        change_state_board(board,"disabled")
        messagebox.showerror("Game Over!","It's a tie")
        if messagebox.askokcancel("Play Again!","Do you want to play again"):
            tieGameBoard = []
            reset_board(board)

def change_state_board(board,state):
    for i in range(9):
        board[i].config(state=state)

def checkWin():
    global winner
    if checkDiag(board)  or checkHoriz(board)  or checkVerti(board) :
        print(f"The winner is {winner}")
        messagebox.showwarning("Winner!!",f"The winner is {winner}")
        change_state_board(board,"disabled")
        if messagebox.askokcancel("Play Again!","Do you want to play again"):
            winner = None
            reset_board(board)
            
##################################################
def create_board(root):
    for i in range(9):
        button = ttkb.Button(root, text="-", width=5, style="secondary.TButton")
       # button = tk.Button(root,text="-", font=custom_font, width=5, height=2)
        if i < 3:
            button.grid(row=0,column=i,sticky="we",pady=5,padx=2)
        elif i > 2 and i < 6:
            button.grid(row=1,column=i-3,sticky="we",pady=2,padx=2)
        elif i > 5 and i < 9:
            button.grid(row=3,column=i-6,sticky="we",pady=2,padx=2)
        button.config(command=lambda btn=button: play_and_switch(btn))
        board.append(button)

def reset_board(board):
    #tieGameBoard= []
    change_state_board(board,"normal")
    for i in range(9):
        board[i].config(text= "-",style="secondary.TButton")
        #board[i].config(style="secondary.TButton")

def close() -> None:
    root.quit()

def center_root_widow() -> None:
    # Fenstergröße festlegen
    fenster_breite = 520
    fenster_hoehe = 380

    # Bildschirmgröße holen
    screen_breite = root.winfo_screenwidth()
    screen_hoehe = root.winfo_screenheight()

    # Koordinaten für zentriertes Fenster berechnen
    x = int((screen_breite / 2) - (fenster_breite / 2))
    y = int((screen_hoehe / 2) - (fenster_hoehe / 2))

    # Geometrie setzen: Breite x Höhe + x + y
    root.geometry(f"{fenster_breite}x{fenster_hoehe}+{x}+{y}")


#root = tk.Tk()
root=ttkb.Window(themename="flatly")
root.title("Tic Tac Toe")
root.geometry("520x380")

style = ttkb.Style()
style.configure('secondary.TButton', font=custom_font, padding=(15, 30))
style.configure('info.TButton', font=custom_font, padding=(15, 30))
style.configure('warning.TButton', font=custom_font, padding=(15, 30))
style.map('warning.TButton', background=[
    ('disabled', '#f0ad4e')], foreground=[('disabled','white')])
style.map('info.TButton', background=[
    ('disabled', '#75caeb')], foreground=[('disabled','white')])
# style.configure("MyCustom.TButton", font=custom_font,bordercolor="gray", background='gray', foreground='white',
#     padding=(15, 30))

menuLeiste = tk.Menu(root)
file_menu = tk.Menu(menuLeiste)
file_menu.add_command(label="Exit", command=close)

play_menu = tk.Menu(menuLeiste)
play_menu.add_command(label="Reset Game", command= lambda : reset_board(board))

menuLeiste.add_cascade(label="File", menu=file_menu)
menuLeiste.add_cascade(label="Game",menu=play_menu)
root.config(menu=menuLeiste)

center_root_widow()
create_board(root)
root.mainloop()