#want to use what i leaned in TTT for mine swweper starting with the board
import tkinter as tk
from tkinter import messagebox
def click(row,col):
    global p
    if L[row][col] == 0:
        L[row][col] = p


L =[[0,0,0],[0,0,0],[0,0,0]] 
root= tk.Tk()
buttons=[[tk.Button(root, text="", font=("Comic Sans MS",32),width=7, height=3, command=lambda row = i, col=j:
                    click(row, col))for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)
e_row = tk.Entry(root)
e_row.grid(row=3,column=0)
e_col = tk.Entry(root)
e_col.grid(row=3,column=1)
