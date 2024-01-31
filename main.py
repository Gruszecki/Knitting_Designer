import tkinter as tk
from tkinter import colorchooser

rows = 10
cols = 10

grid = [[None for _ in range(cols)] for _ in range(rows)]
color = "black"


def on_click(event):
    col = event.x // 20
    row = event.y // 20

    canvas.itemconfig(grid[row][col], fill=color)

def choose_color():
    global color
    color = colorchooser.askcolor()[1]


window = tk.Tk()

canvas = tk.Canvas(window, width=cols*20, height=rows*20)
canvas.pack(side="right")

color_button = tk.Button(window, text="Wybierz kolor", command=choose_color)
color_button.pack(side="left")

for i in range(rows):
    for j in range(cols):
        grid[i][j] = canvas.create_rectangle(j*20, i*20, (j+1)*20, (i+1)*20, fill="white")

canvas.bind("<Button-1>", on_click)

window.mainloop()
