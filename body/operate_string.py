# 3重クオート（文字列を複数行描きたい場合に使う）

print("""
アンパンマンは
何時もバイキンマンを倒してくれて、
町に平和をもたらす
""")

print("---------------------------------------------------------------")

# 文字列の取り出し

hero="""
アンパンマンは
何時もバイキンマンを倒してくれて、
町に平和をもたらす
"""

print(hero[0])
print(hero[1])
print(hero[8])
print(hero[9])
print(hero[27])

print("---------------------------------------------------------------")

# マイナスインデックス（右から数えて要素を取り出す）

author="kafka"
print(author[-1])
print(author[-2])
print(author[-3])

# -1：右から一番目、-3：右から三番目　を取り出す

print("---------------------------------------------------------------")

# 文字列の足し算（連結）

print("cat"+"ting"+" the"+" cat")

print("---------------------------------------------------------------")

# 文字列の掛け算

print("cat!"*3)

print("---------------------------------------------------------------")

# 大文字小文字変換　＆　キャピタライズ（文字列の先頭のみ大文字、それ以外は小文字）

cat="cat"
neko="CAT"

print(cat.upper())

print(neko.lower())

print(cat.capitalize())

print("---------------------------------------------------------------")

# 書式化（フォーマット）　formatメソッド

birth="{}は{}年に生まれました"
name="ウィリアム"
birthday="1897"

print(birth.format(name,birthday))
print(birth.format(birthday,name))

print("---------------------------------------------------------------")

# 入力式　formatメソッド

what=input("何が：")
when=input("いつ：")
where=input("どこで：")
do=input("どうした；")

r="{}は{}に{}で{}。".format(what,when,where,do)
print(r)