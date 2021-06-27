# 分割（splitメソッド）＆　結合[全ての文字列の間に新しい文字列を追加]（joinメソッド）
# 分割：１つの文字列→複数の文字列を「リスト」で返す
# 結合：joinメソッドの引数にリストを渡したとき→「１つの文字列」として出力される

bun="水たまりを飛び込んだんだ。3メートルもあったんだぜ！"
print(bun)
print(bun.split("。"))

first_three="abc"
result="+".join(first_three)
print(result)

words=["The","food","is","very","delisious","."]
connect=" ".join(words)
print(connect)

print("---------------------------------------------------------------")

# 置換（replaceメソッド）

before="All all"
after=before.replace("All","all")
print(after)
print(before.replace("l",""))

print("---------------------------------------------------------------")

# 文字を探す[ある文字列内に含まれている、最初にその文字が現れた位置のインデックス値を返す]
#（indexメソッド）

print(bun.index("水"))
print(bun.index("。"))
print(before.index("all"))

try:
    print(before.index("z"))
except:
    print("not found.")

print("---------------------------------------------------------------")

# 包含[指定した文字列を含んでいるかどうか]（in演算子）

print("cat" in "cat in the hat")
print("hat" not in "cat in the hat")

print("---------------------------------------------------------------")

# エスケープ文字[クオート文字を文字列内に含めたい場合]
# （特定の文字の前に記号を書く　\"）

print("これは\"重要\"です")

print("これは'大切'です")

print("---------------------------------------------------------------")

# 改行（/n）

print("line1\nline2\n\nline3")

print("""line1
line2

line3""")

print("---------------------------------------------------------------")

# スライス[繰り返し可能なオブジェクトの一部分を取り出して、その一部分を新たに出力する]
# (イテラブル（変数）[開始インデックス:終了インデックス])

eigo=["a","b","c","d","e"]
ivan="死の代わりにひとつの光があった。"

print(eigo[0:3])
print(ivan[:6])
print(ivan[6:])
# 開始インデックス位置の要素は含むが、
# 終了インデックス値はその手前の要素までしか含まないことに注意！
