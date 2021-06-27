# Fizz Buzz

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("Fizz Buzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

print("......................................................")

# 線形探索（シンプルな探索アルゴリズムで、要素1つ1つを確認して探索する）

def search(all,hit):
    for j in range(0,all):
        if j==hit:
            return True
    return False

print(search(100,34))
print(search(9,10))
print(search(399,500))

print("......................................................")

# 回文（初めから読んでも終わりから読んでも同じ文章）

def match(word):
    word=word.lower()
    print(word[::-1])
    return word==word[::-1]

print(match("Mom"))
print(match("mother"))
print(match("しんぶんし"))
print(match("新聞紙"))

print("......................................................")

# アナグラム判断（単語の文字を並び替えて、新しい単語を作る）

def anagram(spell1,spell2):
    sort1=sorted(spell1)
    sort2=sorted(spell2)
    print(sort1,sort2)
    return sort1==sort2

print(anagram("iceman","cinema"))
print(anagram("tree","leaf"))

print("......................................................")

# 出現する文字列を数える

def count(counter):
    dic={}
    for x in counter:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1
    return dic

print(count("Dynasty"))

print("......................................................")

# 再帰法（関数からその関数自身を呼び出す手法）

def reback(n):
    if n<1:
        print("No money,no free")
        return
    
    print(str(n)+" money,"+str(n)+" free")
    reback(n-1)

reback(11)

print("......................................................")
