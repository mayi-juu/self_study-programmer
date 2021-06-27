# ハングマンゲームの実装

def hangman(word):
    wrong=0
    stages=["",
    "_____     ",
    "|",
    "|    |    ",
    "|    0    ",
    "|   /|\   ",
    "|   / \   ",
    "|         ",
    ]
    
    # リストは改行しても動作する！

    rletters=list(word)

    # list()関数＝()のなかのオブジェクトを1つずつリストの要素に格納する！

    board=["_"]*len(word)
    # wordの文字数分、"_"の要素を持つリストを作る
    win=False
    print("ハングマンへようこそ！")

    while wrong<len(stages)-1:
        # wrongは0からスタートしていることに注意
        print("\n")
        msg="1文字を予想してね"
        char=input(msg)

        if char in rletters:
            cind=rletters.index(char)
            # inputした文字のrletters内インデックスを取得
            board[cind]=char
            rletters[cind]="$"
            # 同じ文字が複数含まれている場合に、正しいインデックス値がか返ってくるようにするため
        
        else:
            wrong+=1

        print(" ".join(board))
        e=wrong+1
        # 下記スライスに対応させるため
        print("\n".join(stages[:e]))

        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win=True
            break

    if not win:
        # = if True or False:
        print("\n".join(stages[:wrong+1]))
        print("あなたの負け！正解は{}.".format(word))

hangman("cat")