# カプセル化（client:クラスの外から利用するコード、プライベート変数・メソッド、パブリック変数）
# Pythonではcllientからアクセスしてほしくない変数やメソッドには、名前の前にアンダースコアを1つつける

class Data:
    def __init__(self):
        self.nums=[1,2,3,4,5]
        self._unsafe="unsafe"
    
    def change_data(self,index,n):
        self.nums[index]=n

    def _unsafe_method(self):
        print("このメソッドにはアクセスしてはいけません")

data1=Data()
print(data1.nums)
data1.nums[0]=100
print(data1.nums)
    
data2=Data()
data2.change_data(1,200)
print(data2.nums)

print("//////////////////////////////////////////////////////")

print(data1._unsafe)
data1._unsafe_method()

print("......................................................")

# 組み込み関数type(データの型を返す)

print(type("Hello"))
print(type(100))
print(type(3.14))

print("......................................................")

# 他モジュールのクラスを使う（import）
# 継承（メソッド新たに追加＆メソッドオーバーライド）

from importkeishou import Shape

shape1=Shape(10,15)
shape1.size()

class Square(Shape):
    def area(self):
        return self.width*self.len

    def size(self):
        print("変更後　幅：{} , 長さ：{}".format(self.width,self.len))

square1=Square(10,20)
square1.size()
print(square1.area())

print("......................................................")

# コンポジション（別クラスのオブジェクトを変数として持たせる[has-a関係]）

class Dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

class Person:
    def __init__(self,name):
        self.name=name

mick=Person("Mick")
stan=Dog("Stanley","Bulldog",mick)
print(stan.owner.name)

# Personオブジェクトをインスタンス変数ownerに持つ