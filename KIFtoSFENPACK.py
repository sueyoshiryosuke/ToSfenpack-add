import sys
sys.path.append('.')
import os
import Board

#同歩とかの処理
path = "./"+input("ShogiGUIの評価値入りkifファイルがまとめて入ったフォルダをこのプログラムと同じフォルダに入れてから名前を入力してください。\n例：kif\n")
if os.path.exists("./temp"):
    print("tempフォルダがあるようです。削除してからお試しください。")
    input()
    quit()
os.makedirs("./temp")
path2 = "./temp"
files = os.listdir(path)
n=1
while files:
    #kifファイルじゃない…
    if not ".kif" in files[0]:
        n += 1
        if n % 100 == 0:
            print("tempファイル処理…"+str(n)+"ファイル処理済")
        del files[0]
        continue
    rfile = open(path+"/"+files[0], "r")
    wfile = open(path2+"/"+files[0], "w")
    i = 0
    readkif = rfile.readlines()
    while True:
        if "同" in readkif[i] and not("読み筋" in readkif[i]):
            p=1
            while True:
                if "(" in readkif[i-p] and readkif[i-p].find(r"**") == -1 and readkif[i-p].find("同") == -1:
                    moveto0 = readkif[i-p].split()
                    moveto = moveto0[1][:2]
                    wfile.write(readkif[i].replace("同　",moveto))
                    break
                else:
                    p += 1
        else:
             wfile.write(readkif[i])
        if "まで" in readkif[i]:
             break
        i += 1
    rfile.close()
    wfile.close()
    n += 1
    if n % 100 == 0:
        print("tempファイル処理…"+str(n)+"ファイル処理済")
    del files[0]

#ここからsfenpack変換
wfile = open("sfenpack.txt", "w")
path = "./temp"
files = os.listdir(path)
p = 1
while files:
    #kifファイルじゃない…
    if not ".kif" in files[0]:
        n += 1
        if n % 100 == 0:
            print("tempファイル処理…"+str(n)+"ファイル処理済")
        del files[0]
        continue
    board = []
    board = Board.BoardShoki()
    turn = 1
    ply = 1
    #勝ち負け判断
    rfile = open(path+"/"+files[0], "r")
    summary = rfile.read()
    if "で先手の勝ち" in summary or "+詰" in summary :
        result0 = 1
    elif "で後手の勝ち" in summary or "-詰" in summary :
        result0 = -1
    else:
        rfile.close()
        if files:
            del files[0]
        if p % 100 == 0:
            print("変換中…"+str(p)+"棋譜処理済")
        p += 1
        continue
    rfile.close()
    rfile = open(path+"/"+files[0], "r")
    readkif = rfile.readlines()
    #初手まで読み飛ばす
    while True:
        del readkif[0]
        if readkif == [] or readkif[0].split()[0] == "1":
            break
    #終局まで読む
    while readkif:
        #readkifチェック
        if readkif[0].find(r"**") == -1 and "評価値" in readkif[1] and readkif[0].find("投了") == -1 and readkif[0].find("宣言") == -1 and readkif[0].find("持将棋") == -1:
            pass
        else:
            if "まで" in readkif[0] or "まで" in readkif[1] or readkif[0].find("投了") != -1 or readkif[0].find("宣言") != -1 or readkif[0].find("持将棋") != -1:
                break
            sfenmove = Board.kifmove_to_sfenmove(readkif[0].split()[1])
            if turn == 1:
                board = Board.SenteMove(board,sfenmove)
            elif turn == -1:
                board = Board.GoteMove(board,sfenmove)
            turn *= -1
            ply += 1
            while True:
                del readkif[0]
                if readkif[0].find(r"**") == -1:
                    break
            continue         
        #sfen読み込み
        sfen = Board.board_to_sfen(board,turn)
        #sfenmove読み込み
        sfenmove = Board.kifmove_to_sfenmove(readkif[0].split()[1])
        #score読み込み
        score0 = readkif[1].split()[readkif[1].split().index("評価値")+1]
        if "+詰" in score0:
            score = 100000*turn
        elif "-詰" in score0:
            score = -100000*turn
        else:
            score = int(score0.replace("↓",""))*turn
        #result読み込み
        result = str(turn * result0)
        #書き込み
        wfile.write(sfen+"\n"+"move "+sfenmove+"\n"+"score "+str(score)+"\n"+"ply "+str(ply)+"\n"+"result "+result+"\n"+"e\n")
        #board一手進める
        if turn == 1:
            board = Board.SenteMove(board,sfenmove)
        elif turn == -1:
            board = Board.GoteMove(board,sfenmove)
        ply += 1
        #読み進める
        while readkif:
            del readkif[0]
            if readkif == [] or readkif[0].find(r"**") == -1:
                break
        #先手後手交代
        turn *= -1
    rfile.close()
    if files:
        del files[0]
    if p % 100 == 0:
        print("変換中…"+str(p)+"棋譜処理済")
    p += 1
wfile.close()
print("sfenpack出力完了！")
#input()
