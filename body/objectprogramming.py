# print( , , )[カンマ区切り]→1マス開けて出力

pop=[]
pop.append("uta")
pop.append("kashu")
print("pop songs: ",pop)

print("........................................................")

print("cat","dog",2)

print("---------------------------------------------------------------------------------")

# クラス、インスタンス変数、インスタンス化

class Orange:
    def __init__(self,w,c):
        self.weight=w
        self.color=c
        print("Created!")

or1=Orange(10,"dark orange")
or2=Orange(20,"white orange")
or3=Orange(30,"yellow orange")

print(or1.weight)
print(or1.color)
print(or2.weight)
print(or2.color)
print(or3.weight)
print(or3.color)

print("......................................................")

or1.weight=100
or1.color="pink orange"
print(or1.weight)
print(or1.color)

print("---------------------------------------------------------------------------------")

# クラスオブジェクトにメソッドで性質追加(クラス内のメソッドの使い方)

class Apple:
    def __init__(self,w,c):
        self.weight=w
        self.color=c
        self.mold=0
        print("App Created!")

    def rot(self,days,temp):
        self.mold=days*temp

ap1=Apple(200,"red apple")
print("before:",ap1.mold)
ap1.rot(10,28)
print("after:",ap1.mold)

print("---------------------------------------------------------------------------------")

# メソッドによるインスタンス変数の更新（入力による後からの変数変更）

class Square:
    def __init__(self,w,l):
        self.width=w
        self.length=l

    def area(self):
        return self.width*self.length
    
    def change(self,w,l):
        self.width=w
        self.length=l

sq=Square(10,20)
print(sq.area())
sq.change(1,2)
print(sq.area())