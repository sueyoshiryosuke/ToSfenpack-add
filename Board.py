#初期配置
def BoardShoki():
    #0～10：未使用，11～99：盤面，101～107：先手持駒（歩香桂銀金角飛），111～117：後手持駒
    board = ["","","","","","","","","","","",\
             "l","","p","","","","P","","L","",\
             "n","b","p","","","","P","R","N","",\
             "s","","p","","","","P","","S","",\
             "g","","p","","","","P","","G","",\
             "k","","p","","","","P","","K","",\
             "g","","p","","","","P","","G","",\
             "s","","p","","","","P","","S","",\
             "n","r","p","","","","P","B","N","",\
             "l","","p","","","","P","","L","",\
             0,0,0,0,0,0,0,"","","",\
             0,0,0,0,0,0,0,"","",""]
    return board

#盤面表示
def Kyokumen(board):
    linea = '  9   8   7   6   5   4   3   2   1'
    lineb = '-------------------------------------'
    linec = '|   '
    
    line1 =  linec[0:2-int(len(board[91])/2)]+board[91]+linec[1+int(len(board[91])/2+0.6):3]\
            +linec[0:2-int(len(board[81])/2)]+board[81]+linec[1+int(len(board[81])/2+0.6):3]\
            +linec[0:2-int(len(board[71])/2)]+board[71]+linec[1+int(len(board[71])/2+0.6):3]\
            +linec[0:2-int(len(board[61])/2)]+board[61]+linec[1+int(len(board[61])/2+0.6):3]\
            +linec[0:2-int(len(board[51])/2)]+board[51]+linec[1+int(len(board[51])/2+0.6):3]\
            +linec[0:2-int(len(board[41])/2)]+board[41]+linec[1+int(len(board[41])/2+0.6):3]\
            +linec[0:2-int(len(board[31])/2)]+board[31]+linec[1+int(len(board[31])/2+0.6):3]\
            +linec[0:2-int(len(board[21])/2)]+board[21]+linec[1+int(len(board[21])/2+0.6):3]\
            +linec[0:2-int(len(board[11])/2)]+board[11]+linec[1+int(len(board[11])/2+0.6):3]+'|   a'

    line2 =  linec[0:2-int(len(board[92])/2)]+board[92]+linec[1+int(len(board[92])/2+0.6):3]\
            +linec[0:2-int(len(board[82])/2)]+board[82]+linec[1+int(len(board[82])/2+0.6):3]\
            +linec[0:2-int(len(board[72])/2)]+board[72]+linec[1+int(len(board[72])/2+0.6):3]\
            +linec[0:2-int(len(board[62])/2)]+board[62]+linec[1+int(len(board[62])/2+0.6):3]\
            +linec[0:2-int(len(board[52])/2)]+board[52]+linec[1+int(len(board[52])/2+0.6):3]\
            +linec[0:2-int(len(board[42])/2)]+board[42]+linec[1+int(len(board[42])/2+0.6):3]\
            +linec[0:2-int(len(board[32])/2)]+board[32]+linec[1+int(len(board[32])/2+0.6):3]\
            +linec[0:2-int(len(board[22])/2)]+board[22]+linec[1+int(len(board[22])/2+0.6):3]\
            +linec[0:2-int(len(board[12])/2)]+board[12]+linec[1+int(len(board[12])/2+0.6):3]+'|   b'

    line3 =  linec[0:2-int(len(board[93])/2)]+board[93]+linec[1+int(len(board[93])/2+0.6):3]\
            +linec[0:2-int(len(board[83])/2)]+board[83]+linec[1+int(len(board[83])/2+0.6):3]\
            +linec[0:2-int(len(board[73])/2)]+board[73]+linec[1+int(len(board[73])/2+0.6):3]\
            +linec[0:2-int(len(board[63])/2)]+board[63]+linec[1+int(len(board[63])/2+0.6):3]\
            +linec[0:2-int(len(board[53])/2)]+board[53]+linec[1+int(len(board[53])/2+0.6):3]\
            +linec[0:2-int(len(board[43])/2)]+board[43]+linec[1+int(len(board[43])/2+0.6):3]\
            +linec[0:2-int(len(board[33])/2)]+board[33]+linec[1+int(len(board[33])/2+0.6):3]\
            +linec[0:2-int(len(board[23])/2)]+board[23]+linec[1+int(len(board[23])/2+0.6):3]\
            +linec[0:2-int(len(board[13])/2)]+board[13]+linec[1+int(len(board[13])/2+0.6):3]+'|   c'

    line4 =  linec[0:2-int(len(board[94])/2)]+board[94]+linec[1+int(len(board[94])/2+0.6):3]\
            +linec[0:2-int(len(board[84])/2)]+board[84]+linec[1+int(len(board[84])/2+0.6):3]\
            +linec[0:2-int(len(board[74])/2)]+board[74]+linec[1+int(len(board[74])/2+0.6):3]\
            +linec[0:2-int(len(board[64])/2)]+board[64]+linec[1+int(len(board[64])/2+0.6):3]\
            +linec[0:2-int(len(board[54])/2)]+board[54]+linec[1+int(len(board[54])/2+0.6):3]\
            +linec[0:2-int(len(board[44])/2)]+board[44]+linec[1+int(len(board[44])/2+0.6):3]\
            +linec[0:2-int(len(board[34])/2)]+board[34]+linec[1+int(len(board[34])/2+0.6):3]\
            +linec[0:2-int(len(board[24])/2)]+board[24]+linec[1+int(len(board[24])/2+0.6):3]\
            +linec[0:2-int(len(board[14])/2)]+board[14]+linec[1+int(len(board[14])/2+0.6):3]+'|   d'

    line5 =  linec[0:2-int(len(board[95])/2)]+board[95]+linec[1+int(len(board[95])/2+0.6):3]\
            +linec[0:2-int(len(board[85])/2)]+board[85]+linec[1+int(len(board[85])/2+0.6):3]\
            +linec[0:2-int(len(board[75])/2)]+board[75]+linec[1+int(len(board[75])/2+0.6):3]\
            +linec[0:2-int(len(board[65])/2)]+board[65]+linec[1+int(len(board[65])/2+0.6):3]\
            +linec[0:2-int(len(board[55])/2)]+board[55]+linec[1+int(len(board[55])/2+0.6):3]\
            +linec[0:2-int(len(board[45])/2)]+board[45]+linec[1+int(len(board[45])/2+0.6):3]\
            +linec[0:2-int(len(board[35])/2)]+board[35]+linec[1+int(len(board[35])/2+0.6):3]\
            +linec[0:2-int(len(board[25])/2)]+board[25]+linec[1+int(len(board[25])/2+0.6):3]\
            +linec[0:2-int(len(board[15])/2)]+board[15]+linec[1+int(len(board[15])/2+0.6):3]+'|   e'

    line6 =  linec[0:2-int(len(board[96])/2)]+board[96]+linec[1+int(len(board[96])/2+0.6):3]\
            +linec[0:2-int(len(board[86])/2)]+board[86]+linec[1+int(len(board[86])/2+0.6):3]\
            +linec[0:2-int(len(board[76])/2)]+board[76]+linec[1+int(len(board[76])/2+0.6):3]\
            +linec[0:2-int(len(board[66])/2)]+board[66]+linec[1+int(len(board[66])/2+0.6):3]\
            +linec[0:2-int(len(board[56])/2)]+board[56]+linec[1+int(len(board[56])/2+0.6):3]\
            +linec[0:2-int(len(board[46])/2)]+board[46]+linec[1+int(len(board[46])/2+0.6):3]\
            +linec[0:2-int(len(board[36])/2)]+board[36]+linec[1+int(len(board[36])/2+0.6):3]\
            +linec[0:2-int(len(board[26])/2)]+board[26]+linec[1+int(len(board[26])/2+0.6):3]\
            +linec[0:2-int(len(board[16])/2)]+board[16]+linec[1+int(len(board[16])/2+0.6):3]+'|   f'

    line7 =  linec[0:2-int(len(board[97])/2)]+board[97]+linec[1+int(len(board[97])/2+0.6):3]\
            +linec[0:2-int(len(board[87])/2)]+board[87]+linec[1+int(len(board[87])/2+0.6):3]\
            +linec[0:2-int(len(board[77])/2)]+board[77]+linec[1+int(len(board[77])/2+0.6):3]\
            +linec[0:2-int(len(board[67])/2)]+board[67]+linec[1+int(len(board[67])/2+0.6):3]\
            +linec[0:2-int(len(board[57])/2)]+board[57]+linec[1+int(len(board[57])/2+0.6):3]\
            +linec[0:2-int(len(board[47])/2)]+board[47]+linec[1+int(len(board[47])/2+0.6):3]\
            +linec[0:2-int(len(board[37])/2)]+board[37]+linec[1+int(len(board[37])/2+0.6):3]\
            +linec[0:2-int(len(board[27])/2)]+board[27]+linec[1+int(len(board[27])/2+0.6):3]\
            +linec[0:2-int(len(board[17])/2)]+board[17]+linec[1+int(len(board[17])/2+0.6):3]+'|   g'

    line8 =  linec[0:2-int(len(board[98])/2)]+board[98]+linec[1+int(len(board[98])/2+0.6):3]\
            +linec[0:2-int(len(board[88])/2)]+board[88]+linec[1+int(len(board[88])/2+0.6):3]\
            +linec[0:2-int(len(board[78])/2)]+board[78]+linec[1+int(len(board[78])/2+0.6):3]\
            +linec[0:2-int(len(board[68])/2)]+board[68]+linec[1+int(len(board[68])/2+0.6):3]\
            +linec[0:2-int(len(board[58])/2)]+board[58]+linec[1+int(len(board[58])/2+0.6):3]\
            +linec[0:2-int(len(board[48])/2)]+board[48]+linec[1+int(len(board[48])/2+0.6):3]\
            +linec[0:2-int(len(board[38])/2)]+board[38]+linec[1+int(len(board[38])/2+0.6):3]\
            +linec[0:2-int(len(board[28])/2)]+board[28]+linec[1+int(len(board[28])/2+0.6):3]\
            +linec[0:2-int(len(board[18])/2)]+board[18]+linec[1+int(len(board[18])/2+0.6):3]+'|   h'

    line9 =  linec[0:2-int(len(board[99])/2)]+board[99]+linec[1+int(len(board[99])/2+0.6):3]\
            +linec[0:2-int(len(board[89])/2)]+board[89]+linec[1+int(len(board[89])/2+0.6):3]\
            +linec[0:2-int(len(board[79])/2)]+board[79]+linec[1+int(len(board[79])/2+0.6):3]\
            +linec[0:2-int(len(board[69])/2)]+board[69]+linec[1+int(len(board[69])/2+0.6):3]\
            +linec[0:2-int(len(board[59])/2)]+board[59]+linec[1+int(len(board[59])/2+0.6):3]\
            +linec[0:2-int(len(board[49])/2)]+board[49]+linec[1+int(len(board[49])/2+0.6):3]\
            +linec[0:2-int(len(board[39])/2)]+board[39]+linec[1+int(len(board[39])/2+0.6):3]\
            +linec[0:2-int(len(board[29])/2)]+board[29]+linec[1+int(len(board[29])/2+0.6):3]\
            +linec[0:2-int(len(board[19])/2)]+board[19]+linec[1+int(len(board[19])/2+0.6):3]+'|   i'
    
    print('\n' + linea + '\n')
    print(lineb)
    print(line1)
    print(lineb)
    print(line2)
    print(lineb)
    print(line3)
    print(lineb)
    print(line4)
    print(lineb)
    print(line5)
    print(lineb)
    print(line6)
    print(lineb)
    print(line7)
    print(lineb)
    print(line8)
    print(lineb)
    print(line9)
    print(lineb + '\n')
    print("P="+str(board[101])+" L="+str(board[102])+" N="+str(board[103])+" S="+str(board[104])+" G="+str(board[105])+" B="+str(board[106])+" R="+str(board[107])+'\n')
    print("p="+str(board[111])+" l="+str(board[112])+" n="+str(board[113])+" s="+str(board[114])+" g="+str(board[115])+" b="+str(board[116])+" r="+str(board[117])+'\n')


#1a1b→1112への変更
def SfenMoveToNumber(move):
    move = move.translate(str.maketrans({"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9"}))
    return move

#先手の駒を動かす（盤面，指し手）
def SenteMove(board,move):
    move = SfenMoveToNumber(move)
    movefrom = move[:2]
    moveto = move[2:4]
    #駒を打つ際の処理
    if movefrom[1] == "*":
        moveto = int(moveto)
        while True:
            if movefrom[0] == "P":
                board[101] -= 1
                board[moveto] = "P"
                break
            if movefrom[0] == "L":
                board[102] -= 1
                board[moveto] = "L"
                break
            if movefrom[0] == "N":
                board[103] -= 1
                board[moveto] = "N"
                break
            if movefrom[0] == "S":
                board[104] -= 1
                board[moveto] = "S"
                break
            if movefrom[0] == "G":
                board[105] -= 1
                board[moveto] = "G"
                break
            if movefrom[0] == "B":
                board[106] -= 1
                board[moveto] = "B"
                break
            if movefrom[0] == "R":
                board[107] -= 1
                board[moveto] = "R"
                break
        return board
    #駒を動かす場合の処理
    movefrom = int(movefrom)
    moveto = int(moveto)
    #駒を取る処理
    if board[moveto] != "":
        while True:
            if board[moveto][-1] == "p":
                board[101] += 1
                break
            if board[moveto][-1] == "l":
                board[102] += 1
                break
            if board[moveto][-1] == "n":
                board[103] += 1
                break
            if board[moveto][-1] == "s":
                board[104] += 1
                break
            if board[moveto][-1] == "g":
                board[105] += 1
                break
            if board[moveto][-1] == "b":
                board[106] += 1
                break
            if board[moveto][-1] == "r":
                board[107] += 1
                break
    #成る成らず処理
    if move[-1] == "+":
        board[moveto] = "+" + board[movefrom]
    else:
        board[moveto] = board[movefrom]
    board[movefrom] = ""
    return board

#後手の駒を動かす（盤面，指し手）
def GoteMove(board,move):
    move = SfenMoveToNumber(move)
    movefrom = move[:2]
    moveto = move[2:4]
    #駒を打つ際の処理
    if movefrom[1] == "*":
        moveto = int(moveto)
        while True:
            if movefrom[0] == "P":
                board[111] -= 1
                board[moveto] = "p"
                break
            if movefrom[0] == "L":
                board[112] -= 1
                board[moveto] = "l"
                break
            if movefrom[0] == "N":
                board[113] -= 1
                board[moveto] = "n"
                break
            if movefrom[0] == "S":
                board[114] -= 1
                board[moveto] = "s"
                break
            if movefrom[0] == "G":
                board[115] -= 1
                board[moveto] = "g"
                break
            if movefrom[0] == "B":
                board[116] -= 1
                board[moveto] = "b"
                break
            if movefrom[0] == "R":
                board[117] -= 1
                board[moveto] = "r"
                break
        return board
    #駒を動かす場合の処理
    movefrom = int(movefrom)
    moveto = int(moveto)
    #駒を取る処理
    if board[moveto] != "":
        while True:
            if board[moveto][-1] == "P":
                board[111] += 1
                break
            if board[moveto][-1] == "L":
                board[112] += 1
                break
            if board[moveto][-1] == "N":
                board[113] += 1
                break
            if board[moveto][-1] == "S":
                board[114] += 1
                break
            if board[moveto][-1] == "G":
                board[115] += 1
                break
            if board[moveto][-1] == "B":
                board[116] += 1
                break
            if board[moveto][-1] == "R":
                board[117] += 1
                break
    #成る成らず処理
    if move[-1] == "+":
        board[moveto] = "+" + board[movefrom]
    else:
        board[moveto] = board[movefrom]
    board[movefrom] = ""
    return board

#position startpos movesへの対応（"position startpos moves ..."から始まる文字列，進める手数）
def StartposMoves(position , count):
    moves = position.split()
    board = BoardShoki()
    del moves[0:3]
    turn = -1
    tesuu = 0
    for i in moves:
        turn *= -1
        tesuu += 1
        if turn == 1:
            SenteMove(board,i)
        else:
            GoteMove(board,i)
        if tesuu == count:
            return board
    return board

def SenteposMoves(board , sfen):
    sfen = sfen.split()
    turn = -1
    for i in sfen:
        turn *= -1
        if turn == 1:
            SenteMove(board,i)
        else:
            GoteMove(board,i)
    return board

def GoteposMoves(board , sfen):
    sfen = sfen.split()
    turn = 1
    for i in sfen:
        turn *= -1
        if turn == 1:
            SenteMove(board,i)
        else:
            GoteMove(board,i)
    return board

def kifmove_to_sfenmove(move):
    if r")" in move:
        move1 = move[-3]
        move2 = move[-2]
        move2 = move2.translate(str.maketrans({"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i"}))
        move3 = move[0]
        move3 = move3.translate(str.maketrans({"１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9"}))
        move4 = move[1]
        move4 = move4.translate(str.maketrans({"一":"a","二":"b","三":"c","四":"d","五":"e","六":"f","七":"g","八":"h","九":"i"}))
        sfenmove = move1+move2+move3+move4
        if "成" in move:
            sfenmove = sfenmove + r"+"
    elif "打" in move:
        move1 = move[2]
        move1 = move1.translate(str.maketrans({"歩":"P","香":"L","桂":"N","銀":"S","金":"G","角":"B","飛":"R"}))
        move2 = r"*"
        move3 = move[0]
        move3 = move3.translate(str.maketrans({"１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9"}))
        move4 = move[1]
        move4 = move4.translate(str.maketrans({"一":"a","二":"b","三":"c","四":"d","五":"e","六":"f","七":"g","八":"h","九":"i"}))
        sfenmove = move1+move2+move3+move4 
    return sfenmove

def csamove_to_sfenmove(board,move):
    if "00" in move:
        move1 = move[5:7]
        move1 = move1.replace("FU","P").replace("KY","L").replace("KE","N").replace("GI","S").replace("KI","G").replace("KA","B").replace("HI","R")
        move2 = r"*"
        move3 = move[3]
        move4 = move[4]
        move4 = move4.translate(str.maketrans({"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i"}))
        sfenmove = move1+move2+move3+move4
    else:
        move1 = move[1]
        move2 = move[2]
        move2 = move2.translate(str.maketrans({"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i"}))
        move3 = move[3]
        move4 = move[4]
        move4 = move4.translate(str.maketrans({"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i"}))
        sfenmove = move1+move2+move3+move4
        movefrom = sfenmove[:2]
        movefrom = SfenMoveToNumber(movefrom)
        if board[int(movefrom)].upper() == "P" and move[5:7] == "TO":
            sfenmove = sfenmove + r"+"
        elif board[int(movefrom)].upper() == "L" and move[5:7] == "NY":
            sfenmove = sfenmove + r"+"
        elif board[int(movefrom)].upper() == "N" and move[5:7] == "NK":
            sfenmove = sfenmove + r"+"
        elif board[int(movefrom)].upper() == "S" and move[5:7] == "NG":
            sfenmove = sfenmove + r"+"
        elif board[int(movefrom)].upper() == "B" and move[5:7] == "UM":
            sfenmove = sfenmove + r"+"
        elif board[int(movefrom)].upper() == "R" and move[5:7] == "RY":
            sfenmove = sfenmove + r"+"
    return sfenmove

def board_to_sfen(board,turn):
    sfen1 = "sfen"
    sfen2 = ""
    i = 91
    while True:
        sfen0 = board[i]
        if sfen0 == "":
            sfen0 = "0"
        sfen2 = sfen2 + sfen0
        if i == 19:
            break
        elif i < 20:
            sfen2 += "/"
            i += 81
        else:
            i -= 10

    sfen2 = sfen2.replace("000000000","9")
    sfen2 = sfen2.replace("00000000", "8")
    sfen2 = sfen2.replace("0000000",  "7")
    sfen2 = sfen2.replace("000000",   "6")
    sfen2 = sfen2.replace("00000",    "5")
    sfen2 = sfen2.replace("0000",     "4")
    sfen2 = sfen2.replace("000",      "3")
    sfen2 = sfen2.replace("00",       "2")
    sfen2 = sfen2.replace("0",        "1")
    sfen3 = ""
    if turn == 1:
        sfen3 = "b"
    elif turn == -1:
        sfen3 = "w"
    sfen4 = ""
    if board[107] == 1:
        sfen4 += "R"
    elif board[107] > 1:
        sfen4 += str(board[107])+"R"
    if board[106] == 1:
        sfen4 += "B"
    elif board[106] > 1:
        sfen4 += str(board[106])+"B"
    if board[105] == 1:
        sfen4 += "G"
    elif board[105] > 1:
        sfen4 += str(board[105])+"G"
    if board[104] == 1:
        sfen4 += "S"
    elif board[104] > 1:
        sfen4 += str(board[104])+"S"
    if board[103] == 1:
        sfen4 += "N"
    elif board[103] > 1:
        sfen4 += str(board[103])+"N"
    if board[102] == 1:
        sfen4 += "L"
    elif board[102] > 1:
        sfen4 += str(board[102])+"L"
    if board[101] == 1:
        sfen4 += "P"
    elif board[101] > 1:
        sfen4 += str(board[101])+"P"

    if board[117] == 1:
        sfen4 += "r"
    elif board[117] > 1:
        sfen4 += str(board[117])+"r"
    if board[116] == 1:
        sfen4 += "b"
    elif board[116] > 1:
        sfen4 += str(board[116])+"b"
    if board[115] == 1:
        sfen4 += "g"
    elif board[115] > 1:
        sfen4 += str(board[115])+"g"
    if board[114] == 1:
        sfen4 += "s"
    elif board[114] > 1:
        sfen4 += str(board[114])+"s"
    if board[113] == 1:
        sfen4 += "n"
    elif board[113] > 1:
        sfen4 += str(board[113])+"n"
    if board[112] == 1:
        sfen4 += "l"
    elif board[112] > 1:
        sfen4 += str(board[112])+"l"
    if board[111] == 1:
        sfen4 += "p"
    elif board[111] > 1:
        sfen4 += str(board[111])+"p"

    sfen = sfen1 + " " + sfen2 + " " + sfen3 + " " + sfen4 + " " + "0"
    sfen = sfen.replace("  "," - ")
    return sfen
