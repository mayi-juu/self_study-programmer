# ファイルパス取得（osモジュール　os.path.join関数）

import os
print(os.path.join("独学プログラマー","9.file","練習用csv.csv"))
#結果 独学プログラマー\9.file\練習用csv.csv

print("---------------------------------------------------------------")

# ファイルに書き出す（新規ファイルの作成 or 既存ファイルの更新）

with open("st.txt","w",encoding="utf-8") as f:
    f.write("Pythonからこんにちは！")

# 新規作成されたファイルはコードを書き込んでいる「.pyファイル」があるフォルダに保存される

print("---------------------------------------------------------------")

# ファイルから読みこむ
# さらに追加で書き込みしてから読み込む

with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())

print(".........................................")

with open("st.txt","w",encoding="utf-8") as f:
    f.write("wモードで追加")

with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())

# writeメソッドは「上書き」してしまうため、前の内容がすべて消えてしまう！！

print("---------------------------------------------------------------")

# ファイルに追記する（既存の書き込み消える上書き保存ではない）[モード：a]

with open("st.txt","a",encoding="utf-8") as f:
    f.write("aモードで追記")

with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())

print("---------------------------------------------------------------")

# ファイルに改行して追記する（\n）

with open("st.txt","a",encoding="utf-8") as f:
    f.write("\naモードで改行追記")

with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())

print("---------------------------------------------------------------")

# ファイルを読み込んでリストに保存

with open("st.txt","r",encoding="utf-8") as f:
    
    r=f.read()
    for v in r:
        print(v)

print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

with open("st.txt","r",encoding="utf-8") as f:
    print(f.read())

print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。")

mylist1=[]

with open("st.txt","r",encoding="utf-8") as f:

    r=f.read()
    for v in r:
        mylist1.append(v)

print(mylist1)

print("/////////////////////////////////////////////")

mylist2=[]

with open("st.txt","r",encoding="utf-8") as f:
    mylist2.append(f.read())

print(mylist2)

print("/////////////////////////////////////////////")

# 「.txt」ファイルで改行ごとにリストの要素に格納する方法(splitlines()メソッド)

with open("st.txt","r",encoding="utf-8") as f:
    mylist3=f.read().splitlines()
print(mylist3)

print("---------------------------------------------------------------")

# CSVファイルに書き出す（csvモジュール）
# writerメソッド：csvオブジェクトを返す、writerowメソッド：リストの内容をCSVファイルに書き込む

import csv

with open("st.csv","w",newline="") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])

print("---------------------------------------------------------------")

# CSVファイルに追加書き込み（"a"モード）

with open("st.csv","a",newline="") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])

print("---------------------------------------------------------------")

# csvファイルの読み込み
# csv.readerメソッド：csvオブジェクトに変換して読み込む（1行単位で返す！）

with open("st.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(row)

print("/////////////////////////////////////////////")

with open("st.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))

print("---------------------------------------------------------------")

with open("st.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        c=(",".join(row))
        print(c[2])

with open("st.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        c=(",".join(row))
        print(c[-5:-1])

print("---------------------------------------------------------------")

import csv
with open(".\9.file\練習用csv.csv","r",encoding="utf-8") as f:
    r=csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))