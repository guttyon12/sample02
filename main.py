import re
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
                if player == 1:
                    if put_check(j, i) == 0:
                        return

                elif player == -1:
                    if put_check(j, i) == 0:
                        return

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

    # 横の探索

    # 斜めの探索


# 置けるかの確認


def put_check(j, i):
    global data, player

    if player == 1:
        # 上方向のチェック
        if data[j][i-1] == -1 and i > 1:
            for a in range(i-2, 0, -1):

                if data[j][a] == 1:
                    btn[j][i]["text"] = "●"
                    data[j][i] = 1
                    return 1
                if data[j][a] != -1:
                    break

        # 下方向のチェック
        elif data[j][i+1] == -1 and i < 6:
            for a in range(i+2, 7, 1):

                if data[j][a] == 1:
                    btn[j][i]["text"] = "●"
                    data[j][i] = 1
                    return 1
                if data[j][a] != -1:
                    break

        # 右方向のチェック
        elif data[j+1][i] == -1 and j < 6:
            for a in range(j+2, 7, 1):

                if data[a][i] == 1:
                    btn[j][i]["text"] = "●"
                    data[j][i] = 1
                    return 1
                if data[a][i] != -1:
                    break

        # 左方向のチェック
        elif data[j-1][i] == -1 and j > 1:
            for a in range(j-2, 0, -1):

                if data[a][i] == 1:
                    btn[j][i]["text"] = "●"
                    data[j][i] = 1
                    return 1
                if data[a][i] != -1:
                    break

    if player == -1:
        # 上方向のチェック
        if data[j][i-1] == 1 and i > 1:
            for a in range(i-2, 0, -1):

                if data[j][a] == -1:
                    btn[j][i]["text"] = "〇"
                    data[j][i] = -1
                    return 1
                if data[j][a] != 1:
                    break

        # 下方向のチェック
        elif data[j][i+1] == 1 and i < 6:
            for a in range(i+2, 7, 1):

                if data[j][a] == -1:
                    btn[j][i]["text"] = "〇"
                    data[j][i] = -1
                    return 1
                if data[j][a] != 1:
                    break

        # 右方向のチェック
        elif data[j+1][i] == 1 and j < 6:
            for a in range(j+2, 7, 1):

                if data[a][i] == -1:
                    btn[j][i]["text"] = "〇"
                    data[j][i] = -1
                    return 1
                if data[a][i] != 1:
                    break

        # 左方向のチェック
        elif data[j-1][i] == 1 and j > 1:
            for a in range(j-2, 0, -1):

                if data[a][i] == 1:
                    btn[j][i]["text"] = "〇"
                    data[j][i] = -1
                    return 1
                if data[a][i] != 1:
                    break

    return 0


# 裏返す関数
def reverse(j, i):
    global data, player

    if player == 1:
        # 上方向
        if data[j][i-1] == -1 and i > 1:
            for a in range(i-2, 0, -1):

                if data[j][a] == 1:
                    for b in range(a, i-1, 1):
                        btn[j][b]["text"] = "●"
                        data[j][b] = 1

        # 下方向
        if data[j][i+1] == -1 and i < 6:
            for a in range(i+2, 7, 1):

                if data[j][a] == 1:
                    for b in range(a, i+1, -1):
                        btn[j][b]["text"] = "●"
                        data[j][b] = 1

        # 右方向
        if data[j+1][i] == -1 and j < 6:
            for a in range(j+2, 7, 1):

                if data[a][i] == 1:
                    for b in range(a, j+1, -1):
                        btn[b][i]["text"] = "●"
                        data[b][i] = 1

        # 左方向
        if data[j-1][i] == -1 and j > 1:
            for a in range(j-2, 0, -1):

                if data[a][i] == 1:
                    for b in range(a, j-1, 1):
                        btn[b][i]["text"] = "●"
                        data[b][i] = 1


# プレイヤーの変更
def turn():
    global player
    return player * (-1)


def init_text():
    global btn
    for i in range(8):
        for j in range(8):
            btn[i][j]["text"] = ""


root = tk.Tk()
root.title("リーバーシ")
# player 1 は黒 -1は白
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

init_data()


root.bind("<ButtonPress>", check)

root.mainloop()
