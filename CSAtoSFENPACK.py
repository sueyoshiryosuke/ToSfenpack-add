import sys
sys.path.append('.')
import os
import Board

wfile = open("sfenpack.txt", "w")
path = "./"+input("floodgateのcsaファイルがまとめて入ったフォルダをこのプログラムと同じフォルダに入れてから名前を入力してください。\n例：csa\n")
files = os.listdir(path)

p = 1
while files:
    #csaファイルじゃない…
    if not ".csa" in files[0]:
        del files[0]
        if p % 100 == 0:
            print("変換中…"+str(p)+"棋譜処理済")
        p += 1
        continue
    board = []
    board = Board.BoardShoki()
    turn = 1
    ply = 1
    #勝ち負け判断
    rfile = open(path+"/"+files[0], "r")
    summary = rfile.read()
    if "draw:" in summary or "abnormal:" in summary or "time_up:" in summary:
        rfile.close()
        del files[0]
        if p % 100 == 0:
            print("変換中…"+str(p)+"棋譜処理済")
        p += 1
        continue
    elif "win:" in summary:
        result0 = 1
    elif "lose:" in summary:
        result0 = -1
    rfile.close()
    rfile = open(path+"/"+files[0], "r")
    readkif = rfile.readlines()
    #初手まで読み飛ばす
    while True:
        if "rating:" in readkif[0]:
            break
        del readkif[0]
    while True:
        del readkif[0]
        if readkif == [] or readkif[0].find("+") == 0:
            break
    #終局まで読む
    while readkif:
        #readkifチェック
        if (readkif[0].find("+") == 0 or readkif[0].find("-") == 0) and "T" in readkif[1] and r"'**" in readkif[2]:
            pass
        else:
            if "%" in readkif[0] or "%" in readkif[1] or "%" in readkif[2]:
                break
            sfenmove = Board.csamove_to_sfenmove(board,readkif[0])
            if turn == 1:
                board = Board.SenteMove(board,sfenmove)
            elif turn == -1:
                board = Board.GoteMove(board,sfenmove)
            turn *= -1
            ply += 1
            while True:
                del readkif[0]
                if readkif[0].find("+") == 0 or readkif[0].find("-") == 0:
                    break
            continue         
        #sfen読み込み
        sfen = Board.board_to_sfen(board,turn)
        #sfenmove読み込み
        sfenmove = Board.csamove_to_sfenmove(board,readkif[0])
        #score読み込み
        score0 = readkif[2].split()
        score = str(int(score0[1]) * turn)
        #result読み込み
        result = str(turn * result0)
        #書き込み
        wfile.write(sfen+"\n"+"move "+sfenmove+"\n"+"score "+score+"\n"+"ply "+str(ply)+"\n"+"result "+result+"\n"+"e\n")
        #board一手進める
        if turn == 1:
            board = Board.SenteMove(board,sfenmove)
        elif turn == -1:
            board = Board.GoteMove(board,sfenmove)
        ply += 1
        #次の手まで読む
        while readkif:
            del readkif[0]
            if readkif == [] or readkif[0].find("+") == 0 or readkif[0].find("-") == 0:
                break
        #先手後手交代
        turn *= -1
    rfile.close()
    del files[0]
    if p % 100 == 0:
        print("変換中…"+str(p)+"棋譜処理済")
    p += 1
wfile.close()
print("sfenpack出力完了！")
#input()
