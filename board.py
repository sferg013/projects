import tkinter as tk
from tkinter import messagebox
def coords():
    x=int(e_row.get())
    y=int(e_col.get())
    if L[x][y]==0:
        return(x,y)
    else:
        messagebox.showinfo("try again")
        return None
def update():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=symbols[L[i][j]])
def win():
    for p in [1, 2]:
        for i in range(3):
            if all(L[i][j] == p for j in range(3)) or all(L[j][i] == p for j in range(3)):
                messagebox.showinfo(f"Player {p} wins")
                reset()
        if all(L[i][i] == p for i in range(3)) or all(L[i][2 - i] == p for i in range(3)):
            messagebox.showinfo(f"Player {p} wins")
            reset()

def reset():
    global L, p
    L =[[0,0,0],[0,0,0],[0,0,0]]
    p=1
    update()

def click(row,col):
    global p
    if L[row][col] == 0:
        L[row][col] = p
        update()
        win()
        p=3-p 

L =[[0,0,0],[0,0,0],[0,0,0]]
symbols = {0: "", 1: "X", 2: "O"}
root= tk.Tk()
p=1
buttons=[[tk.Button(root, text="", font=("Comic Sans MS",32),width=7, height=3, command=lambda row = i, col=j:
                    click(row, col))for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

e_row = tk.Entry(root)
e_row.grid(row=3,column=0)
e_col = tk.Entry(root)
e_col.grid(row=3,column=1)

move = tk.Button(root, text="Make Move", command=lambda: click(*coords()))
move.grid(row=3, column=2)
reset= tk.Button(root,text="Reset", command=reset)
reset.grid(row=4,column=0,columnspan=3)

root.mainloop()