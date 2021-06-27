# クラスオブジェクト（Pythonではどのクラスもオブジェクト！[typeクラスのインスタンス]）
# とクラス変数（クラスオブジェクトに属す）

class Rectangle:
    recs=[]
    #クラス変数（クラスのスイート部最初に書く？！[__init__の外]）

    def __init__(self,w,l):
        self.wid=w
        self.len=l
        self.recs.append((self.wid,self.len))
        # クラス変数にアクセスするときは「self.」を変数の前につける！

    def size(self):
        print("{} by {}".format(self.wid,self.len))

r1=Rectangle(10,24)
r2=Rectangle(20,40)
r3=Rectangle(100,200)

print(Rectangle)
print(Rectangle(1,2))
# 上部はRectangleというクラスオブジェクトを出力している
# 下部はRectangleクラスのインスタンスオブジェクトを出力している

print("////////////////////////////////////////////////////////////////////")

print(Rectangle.recs)
print(r2.recs)
# クラス変数はクラスオブジェクト（上）、インスタンスオブジェクト（下）どちらからも呼び出せる！
# クラス変数はクラスのインスタンスが生成されるたびに追加される！！

print("......................................................")

# 特殊メソッド __repr__ のオーバーライド
# 全てのクラスはobjectクラスを継承しており、objectクラスから継承した__repr__も呼び出せる

class Lion1:
    def __init__(self,name):
        self.name=name

lion1=Lion1("dante")
print(lion1)

print("/////////////////////////////////////////////////////////////////////")

class Lion2:
    def __init__(self,name):
        self.name=name

    def __repr__(self):
        return self.name

lion2=Lion2("dante")
print(lion2)

# 変な文字列の集まりではなく、既定の処理（今回の場合は名前：danteを出力）に変えられる！

print("......................................................")

# オブジェクト（被演算子）の特殊メソッド→演算をするときに自動的に呼び出される！
# 生成したオブジェクトを演算できるようにしたいならば、その計算したい種類の特殊メソッドを持たせる！

# 足し算 __add__(self,other[何でもよい？！])

class Wa:
    def __init__(self,num):
        self.n=num

    def __add__(self,other):
        return abs(self.n+other.n)
        # abs:絶対値

x=Wa(-20)
y=Wa(10)
print(x+y)

class Wa:
    def __init__(self,num):
        self.n=num

    def __add__(self,other):
        return self.n+other.n

x=Wa(-20)
y=Wa(10)
print(x+y)

print("//////////////////////////////////////////////////////////")

# 比較（引数の方が大、オブジェクトの値の方が小さい）__lt__(self,other[何でもよい？！])

class Cardbig:
    def __init__(self,v):
        self.val=v

    def __lt__(self,other):
        if self.val<other.val:
            return True
        return False

a=Cardbig(5)
b=Cardbig(2)
print(b<a)
print(a<b)

print("//////////////////////////////////////////////////////////")

# 比較（引数の方が小、オブジェクトの値の方が大きい）__gt__(self,other[何でもよい？！])

class Cardsmall:
    def __init__(self,v):
        self.val=v

    def __gt__(self,other):
        if self.val>other.val:
            return True
        return False

c=Cardbig(-2)
d=Cardbig(-5)
print(c>d)
print(d>c)

print("......................................................")

# is (前後のオブジェクトが同一のオブジェクトならTrue、同じでないならFalseを返す)
# ※ある変数がNoneかどうかを調べるときにも使う

r4=r1
print(r1 is r4)
print(r1 is r2)

print("//////////////////////////////////////////////////////////")

class Person:
    def __init__(self):
        self.name="Bob"

bob=Person()
same_bob=bob
another_bob=Person()

print(bob is same_bob)
print(bob is another_bob)

print("//////////////////////////////////////////////////////////")

p=10
if p is None:
    print("pはNoneです")
else:
    print("pはNoneではない")

p=None
if p is None:
    print("pはNoneです")
else:
    print("pはNoneではない")
