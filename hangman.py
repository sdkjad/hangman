import random

def hangman():                     #関数定義

    wordlist = ["cat","dog","red","blue"]
    n = len(wordlist)
    random_number = random.randint(0,n)
    word = wordlist[random_number]

    wrong = 0                          #worng に 0
    stages = ["",                      #stage

             "________        ",

             "|               ",

             "|        |      ",

             "|        0      ",

             "|       /|\     ",

             "|       / \     ",

             "|               "

              ]

    rletters = list(word)                #残りの文字をrlettersのリストに入れる
    board = ["_"] * len(word)            #ヒント['_', '_', '_']
    win = False                          #winにFalseを入れる
    print("ハングマンへようこそ")        #あいさつ

    while wrong < len(stages)-1:         #間違いがステージの行数(8)より少ない間は繰り返す
        print("\n")                      #改行
        msg = "文字を予想してね"         #"文字を予想してね"
        char = input(msg)                #入力した文字をcharに入れる

        if char in rletters:             #あたりのとき　入力した文字がrlettersの中にある
            cind = rletters.index(char)  #入力した文字は何文字目か
            board[cind] = char           #入力した文字をboardの該当文字に置き換える
            rletters[cind] = "$"              #rlettersで当たったものを$に置き換える

        else:
            wrong += 1                   #はずれのとき　wrongを一つ増やす

        print(" ".join(board))
        e = wrong +1
        print("\n".join(stages[0:e]))


        if "_" not in board:             #全部当たりのとき　boardに_がなくなると
            print("あなたの勝ち")        #あなたの勝ち
            print(" ".join(board))       #boardを表示
            win = True                   #winにTrueを入れる
            break                        #ループから出る

    if not win:                          #ループの外
        print("\n".join(stages))  #stagesのリストを改行で繋げて表示
        print("あなたの負け！正解は{}".format(word)) #m負けと表示

hangman()

        
