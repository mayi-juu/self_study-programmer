# データ構造：スタックを実際にプログラミングしてみる（要素の追加や削除がリストの終端でしか行えない）

class Stack:
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

stack=Stack()
print(stack.is_empty())
print(stack.items)

stack.push(1)
print(stack.items)
print(stack.is_empty())

print("del:"+str(stack.pop()))
print(stack.is_empty())

print("/////////////////////////////////////////////////////")

for i in range(0,6):
    stack.push(i)

print(stack.items)
print(stack.peek())
print(stack.size())

print("......................................................")

stack.items=[]

# スタックを使って文字列を逆順にする

for h in "Hello":
    stack.push(h)
print(stack.items)

reverse=""
while stack.size()>0:
    reverse+=stack.pop()
print(reverse)
print(stack.items)

print("......................................................")

# データ構造：キューを実際にプログラミングしてみる（最初に入れた要素が一番初めに取り出される）

class Queue:
    def __init__(self):
        self.itemss=[]
    
    def is_empty(self):
        return self.itemss==[]

    def enqueue(self,item):
        self.itemss.insert(0,item)

    def dequeue(self):
        return self.itemss.pop()

    def size(self):
        return len(self.itemss)

que=Queue()
print(que.is_empty())

for j in range(5):
    que.enqueue(j)
print(que.itemss)
print(que.size())

while que.size():
    print(que.dequeue())
    print(que.itemss)

print("......................................................")

# チケット行列（映画のチケットを買う待ち行列をプログラミングで表現）

import time
import random

# 上記のQueueクラスを使用

def simu(till_show,max_time):
    wait=Queue()
    sold=[]

    for i in range(100):
        wait.enqueue("person:"+str(i))
    """
    print(wait.itemss)
    return wait.dequeue()
    """
    t_end=time.time()+till_show
    now=time.time()
    # time.timeメソッド：epockからの経過時間を返す
    
    while now<t_end and not wait.is_empty():
        now=time.time()
        r=random.randint(0,max_time)
        time.sleep(r)
        person=wait.dequeue()
        print(person)
        sold.append(person)
    return sold
        # time.sleep(r):Pythonの処理をr秒だけ一時停止する

ticket=simu(5,1)
print(ticket)