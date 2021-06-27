# 3引数関数

def f(x,y,z):
    return x+y+z

result=f(5,3,2)

if result==10:
    print("合計値は10です")
else:
    print("10ではありません")

print("---------------------------------------------------------------")

# input文

age=input("貴方の年齢を入力してください：")
int_age=int(age)

if int_age<21:
    print("割引価格でご利用できます")
else:
    print("通常料金です")

print("---------------------------------------------------------------")

#　input文を組み込んだ関数定義(※引数に注意！！)

def even_odd():
    n=input("type a number:")
    n=int(n)
    if n%2==0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd()
even_odd()
even_odd()

print("---------------------------------------------------------------")



print("---------------------------------------------------------------")

#　改良：input文を組み込んだ関数定義(※引数に注意！！)

def even_odd(sentence):
    n=input(sentence)
    n=int(n)
    if n%2==0:
        print("n is even.")
    else:
        print("n is odd.")

even_odd("年齢は?")
even_odd("身長は?")
even_odd("体重は?")

print("---------------------------------------------------------------")

# 関数の初期値

def add_it(x,y=10):
    return x+y

result=add_it(2)
print(result)
print(add_it(2,5))

print("---------------------------------------------------------------")

# ローカルスコープの中からグルーバル変数に書き込む方法

x=100
def f():
    global x
    x+=1
    print(x)
f()

print("---------------------------------------------------------------")

# 例外処理

a=int(input("number?:"))
b=int(input("another number?（0を入力してください）:"))
print(a/b)

print("---------------------------------------------------------------")

# 例外処理 try, except

a=int(input("number?:"))
b=int(input("another number?（0を入力してください）:"))
try:
    print(a/b)
except (ZeroDivisionError):
    print("0は入力できません")

print("---------------------------------------------------------------")

# 例外処理 try, except 2

a=int(input("number?:"))
b=int(input("another number?（0を入力してください）:"))
try:
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("正しい数値を入力してください")

# ドキュメンテーション文字列（関数の説明）

def add(x,y):
    """
    Returns x+y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return(x+y)
print(add(2,3))
