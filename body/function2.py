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
