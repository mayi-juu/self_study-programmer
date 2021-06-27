# forループ（文字列ー1文字ずつ出力）

name="Jenny"
for character in name:
    print(character)


print("---------------------------------------------------------------")

# forループ（タプル）

drinks=("COLA","PEPshi","METs")
for drink in drinks:
    print(drink)

print("---------------------------------------------------------------")

# リストの更新

foods=["rice","bread","paste"]

i=0
for food in foods:
    foods[i]=food.upper()
    i+=1
print(foods)

print("---------------------------------------------------------------")

# forループの中でデータを加工して、別のリストに追加する

trainings=["MUSTLE","RUN","STRETCH"]

sets=[]
sets.append(foods)
sets.append(trainings)
print(sets)

sets2=[]

for food in foods:
    food=food.upper()
    sets2.append(food)

for training in trainings:
    training=training.lower()
    sets2.append(training)

print(sets2)

print("---------------------------------------------------------------")

# range関数 （整数を順番に生成してくれる。これをforループに渡して繰り返しに使える）
# ※引数の2つ目の値は処理に含まれない

for i in range(1,6):
    print(i)

print("---------------------------------------------------------------")

# whileループ

x=5
while x>0:
    print(x)
    x-=1
print("Happy New Year!")

print("---------------------------------------------------------------")

# break文(qが入力されるまで3つの質問を繰り返す)

qu=["名前？","身長？","体重？"]

n=0
print("入力を終了したい場合、「q」キーを入力してください:")
matome=[]

while True:
    ques=input(qu[n])
    if ques=="q":
        print("入力が終了しました。")
        print(matome)
        break

    out=qu[n]
    segment=out[:2]+":"+ques
    matome.append(segment)
    n=(n+1)%3

print("---------------------------------------------------------------")

# continue文（それ以降のコードは実行されず、すぐ次のループが始まる）

i=1
while i<=5:
    if i==3:
        i +=1
        continue
    print(i)
    i += 1

print("---------------------------------------------------------------")

# 入れ子のループ（外側のループが１回回るごとに、内側のループが全部回る）

for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)

print("---------------------------------------------------------------")

# 入れ子 ２つのリストの数値それぞれの全ての組み合わせを足し算した結果を、新しいリストに格納する

list1=[1,2,3,4]
list2=[5,6,7,8]
added=[]

for x in list1:
    for y in list2:
        added.append(x+y)
print(added)
