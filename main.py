import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox

# 初期化


def init_data():
    global init, data
    data = [[init for i in range(8)] for j in range(8)]
    data[3][3] = 1
    btn[3][3]["text"] = "●"
    data[4][3] = -1
    btn[4][3]["text"] = "〇"
    data[4][4] = 1
    btn[4][4]["text"] = "●"
    data[3][4] = -1
    btn[3][4]["text"] = "〇"


def check(e):
    global data, player
    for i in range(8):
        for j in range(8):
            if e.widget == btn[j][i]:
                if player == 1 and put_check(i, j) == 1:
                    e.widget["text"] = "●"
                    data[j][i] = 1
                elif player == -1:
                    e.widget["text"] = "〇"
                    data[j][i] = -1

    player = turn()

    if judge() == 1:
        messagebox.showinfo('ゲーム終了', "先行の勝利")
        init_data()
        init_text()
    elif judge() == -1:
        messagebox.showinfo('ゲーム終了', "後攻の勝利")
        init_data()
        init_text()
    elif judge() == -2:
        messagebox.showinfo('ゲーム終了', "引き分け")
        init_data()
        init_text()


def judge():
    global data
    # 縦の探索
    for i in range(3):
        if data[i][0] != 0:
            if data[i][0] == data[i][1] and data[i][0] == data[i][2]:
                return data[i][0]

    # 横の探索
    for j in range(3):
        if data[0][j] != 0:
            if data[0][j] == data[1][j] and data[0][j] == data[2][j]:
                return data[0][j]

    # 斜めの探索
    if data[1][1] != 0:
        if data[0][0] == data[1][1] and data[0][0] == data[2][2]:
            return data[1][1]
        elif data[0][2] == data[1][1] and data[0][2] == data[2][0]:
            return data[1][1]

    for i in range(3):
        for j in range(3):
            if data[j][i] == 0:
                return 0

    return -2

# 置けるかの確認


def put_check(i, j):
    global data, player

    if player == 1:
        if data[i][j-1] == -1:
            for a in range(j-2, 0, -1):

    if player == -1:

        # プレイヤーの変更


def turn():
    global player
    return player * (-1)


def init_text():
    global btn
    for i in range(3):
        for j in range(3):
            btn[i][j]["text"] = ""


root = tk.Tk()
root.title("リーバーシ")

player = 1

init = 0
data = [[init for i in range(8)] for j in range(8)]

w = 15
h = 5

btn = [[tk.Button(root, width=w, height=h) for i in range(8)]
       for j in range(8)]

for i in range(8):
    for j in range(8):
        btn[j][i].grid(column=j, row=i)

data[3][3] = 1
btn[3][3]["text"] = "●"
data[4][3] = -1
btn[4][3]["text"] = "〇"
data[4][4] = 1
btn[4][4]["text"] = "●"
data[3][4] = -1
btn[3][4]["text"] = "〇"


root.bind("<ButtonPress>", check)

root.mainloop()
