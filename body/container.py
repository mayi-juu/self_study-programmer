# リスト範囲外エラー

colors=["blue","green","yellow"]
try:
    print(colors[3])
except IndexError:
    print("リストにリテラルが存在していません")

print("---------------------------------------------------------------")

# popメソッド（リストの末尾から要素を取り除く）

print(colors)

colors.pop()
print(colors)

colors.append("red")
print(colors)

print("---------------------------------------------------------------")

# リストの連結

colors2=["青","緑","赤"]
newcolors=colors+colors2
print(newcolors)

print("---------------------------------------------------------------")

# ある要素がリストに含まれているか・いないかの確認方法
# in 演算子とnot in 演算子

print("green" in newcolors)
print("black" in newcolors)

print("black" not in newcolors)
print("緑" not in newcolors)

#出力結果は True or False

print("---------------------------------------------------------------")

# リストのサイズの調べ方
# len関数
print(len(newcolors))

print("---------------------------------------------------------------")

# 色当てクイズ

print(colors)

guess=input("上記のうち1つでも日本語で何色でしょう？：")
if guess in colors2:
    print("よくできました！")
else:
    print("もう少しお勉強が必要です・・・")

print("---------------------------------------------------------------")

# タプル（リストとの相違点：イミュータブル[変更不可能]）

points=(10,20,30)
print(points[1])
print(4 in points)
print(20 not in points)
