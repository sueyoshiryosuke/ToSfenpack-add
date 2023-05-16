# Electron将棋の出力kifファイル用、やねうら王の教師データ変換プログラム
import sys
sys.path.append('.')
import os
import Board
import re

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
    
    readkif = rfile.readlines()
    turn_player = 1  # その手番のプレーヤー。1は先手、-1は後手。
    for readkif_line in readkif:
        if "手詰" in readkif_line:
            mate_depth = int(re.findall(r'\d+', readkif_line)[0])
            if now_player == 1:  # 先手番
                if mate_depth%2==1:
                    wfile.write(f"**対局 評価値 +詰 {mate_depth} 読み筋 none\n")
                else:
                    wfile.write(f"**対局 評価値 -詰 {mate_depth} 読み筋 none\n")
            else:
                if mate_depth%2==1:
                    wfile.write(f"**対局 評価値 -詰 {mate_depth} 読み筋 none\n")
                else:
                    wfile.write(f"**対局 評価値 +詰 {mate_depth} 読み筋 none\n")
            
            if   mate_depth == 1 and now_player == 1:
                wfile.write(f"{turn_num+1} 投了 ( 0:00/0:00:00) \n")
                wfile.write(f"まで{turn_num+1}手で先手の勝ち\n")
                break
            elif mate_depth == 1 and now_player == -1:
                wfile.write(f"{turn_num+1} 投了 ( 0:00/0:00:00)\n")
                wfile.write(f"まで{turn_num+1}手で後手の勝ち\n")
                break
            continue
        elif "先手番" in readkif_line:
            first_player = 1   # 初手（1手目）のプレーヤー。1は先手、-1は後手。
        elif "後手番" in readkif_line:
            first_player = -1  # 初手（1手目）のプレーヤー。1は先手、-1は後手。
        elif " ( " in readkif_line:
            turn_num = int(readkif_line.split()[0])  # 手数
            if turn_num%2==1:
                now_player =  first_player # その手番のプレーヤー。1は先手、-1は後手。
            else:
                now_player = -first_player # その手番のプレーヤー。1は先手、-1は後手。
            if "千日手" in readkif_line or "持将棋" in readkif_line:
                wfile.write(readkif_line)
                wfile.write("まで\n")
                break
        # 「読み筋」の行はスキップする。
        elif "**読み筋" in readkif_line:
            continue
        # 「**」ではなく「*」から始まる行はスキップする。
        elif readkif_line[0]=="*" and readkif_line[1]!="*":
            continue
        elif "評価値" in readkif_line:
            readkif_line = readkif_line[:-1] + " 読み筋 \n"
        else:
            pass
        write_line = readkif_line.replace("**評価値=", "**対局 評価値 ")
        wfile.write(write_line)
    rfile.close()
    wfile.close()
    n += 1
    if n % 100 == 0:
        print("tempファイル処理…"+str(n)+"ファイル処理済")
    del files[0]

#ここからsfenpack変換
path = "./temp"
files = os.listdir(path)
p = 1
result_list = []  # 各kifファイルごとの勝敗リスト。勝ち1、負け-1、引き分け0。
for file_names in files:
#while files:
    #kifファイルじゃない…
    if not ".kif" in file_names:
        print(f"{file_names}はkifファイルではないのでスキップします。")
        files.remove(file_names)
        continue
    #勝ち負け判断
    rfile = open(path+"/"+file_names, "r")
    summary = rfile.read()
    if "で先手の勝ち" in summary:
        #result0 = 1
        result_list.append(1)
    elif "で後手の勝ち" in summary:
        #result0 = -1
        result_list.append(-1)
    elif "千日手" in summary or "持将棋" in summary:
        #result0 = 0
        result_list.append(0)
    else:
        rfile.close()
        print(f"{file_names}は勝ち負け以外の結果なのでスキップします。")
        files.remove(file_names)
        continue
    rfile.close()

i=0
if(os.path.isfile('sfenpack.txt')):
    os.remove('sfenpack.txt')
for file_names in files:
    board = []
    board = Board.BoardShoki()
    turn = 1
    ply = 1

    wfile = open("sfenpack.txt", "a")
    rfile = open(path+"/"+file_names, "r")
    readkif = rfile.readlines()
    #初手まで読み飛ばす
    while True:
        if readkif == [] or readkif[0].split()[0] == "1":
            break
        del readkif[0]
    #終局まで読む
    while readkif:
        #readkifチェック
        if readkif[0].find(r"**") == -1 and "評価値" in readkif[1] and readkif[0].find("投了") == -1 and readkif[0].find("宣言") == -1 and readkif[0].find("持将棋") == -1:
            pass
        else:
            if "まで" in readkif[0] or "まで" in readkif[1] or readkif[0].find("投了") != -1 or readkif[0].find("宣言") != -1 or readkif[0].find("持将棋") != -1:
                i += 1
                break
            readkif.insert(1, "**対局 評価値 0 読み筋 \n")
        
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
        result = str(turn * result_list[i])
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
    wfile.close()

    if p % 100 == 0:
        print("変換中…"+str(p)+"棋譜処理済")
    p += 1
print("sfenpack出力完了！")
#input()
