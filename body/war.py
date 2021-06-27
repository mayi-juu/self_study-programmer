# カードゲーム「戦(争」

class Card:
    suits=["spades","hearts","diamonds","clubs"]
    values=[None,None,
    "2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]
    # クラス変数
    # valuesの最初の2つの要素にNoneを持たせているのは、リストのインデックス操作と値を一致させるため
    # マークの強さはsuitsリストに並んでいる順番、すなわちインデックスの値で決まるように工夫している！

    def __init__(self,v,s):
        self.value=v
        self.suit=s
        # バリューもスート（マーク）も整数値！（比較や計算、リスト取り出しを行いやすくするため！）

    def __lt__(self,c2):
        if self.value<c2.value:
            return True
        if self.value==c2.value:
            if self.suit<c2.suit:
                return True
            else:
                return False
        return False
        # 小なり比較できるように定義（比較演算子はTrueかFalseが出力される）

    def __gt__(self,c2):
        if self.value>c2.value:
            return True
        if self.value==c2.value:
            if self.suit>c2.suit:
                return True
            else:
                return False
        return False
        # 大なり比較できるように定義（比較演算子はTrueかFalseが出力される）

    def __repr__(self):
        return "マーク：{}、値：{}".format(self.suits[self.suit],self.values[self.value])
    # __repr__を定義するのは、Deckクラスのオブジェクトを生成した後に、
    # カード情報を簡単に出力するため

"""
card1=Card(9,1)
card2=Card(3,0)
print(card1>card2)
print(card1<card2)
print(card1)
"""

from random import shuffle

class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(0,4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
        # self.cardsのリストの中に５２枚のカード情報を追加、
        # そしてその各要素をリスト内でシャッフルして順番をバラバラにする

    def rm_card(self):
        if len(self.cards)==0:
            return 
            # return 「None」が省略されてる！
        return self.cards.pop()
        """
        pop()について
        　→指定した位置の要素を削除し、その値を取得するメソッド
        　ex.
           l=[0,1,2,3,4]
           print(l.pop(0))⇒#0
           print(l)⇒#[1,2,3,4]
        ※()内が空白の場合、リストの末尾（最後）の要素を削除
        """

"""
deck=Deck()

for card in deck.cards:
    print(card)

print("/////////////////////////////////////////")
print(deck.rm_card())
print("/////////////////////////////////////////")

for card in deck.cards:
    print(card)
"""

class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        name1=input("プレーヤー1の名前：")
        name2=input("プレーヤー2の名前：")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def wins(self,winner):
        w="このラウンドは{}が勝ちました"
        w=w.format(winner)
        print(w)
    
    def draw(self,p1n,p1c,p2n,p2c):
        d="{}は{}、{}は{}を引きました"
        d=d.format(p1n,p1c,p2n,p2c)
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("戦争を始めます！")
        
        while len(cards)>=2:
            m="qで終了、それ以外のキーでプレイ："
            response=input(m)
            if response=="q":
                break
            
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            # 「drawメソッド」のp1c,p2c,p1n,p2nとはまた別！（変数として定義！）

            #下記　「Cardクラス」において、
            #インスタンス化したオブジェクトが大小比較できるようにしたから計算できる！
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)

        win=self.winner(self.p1,self.p2)
        if win=="引き分け！":
            print("引き分け！")
        else:
            print("ゲーム終了、{}の勝利です！".format(win))

    # 先に使う予定のメソッドをコーディングし、後からそのメソッドを定義しても良い！（処理順）
    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "引き分け！"

game=Game()
game.play_game()