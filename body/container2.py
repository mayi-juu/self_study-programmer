# 辞書

items={"sweet":100,"ice":150}
items["dish"]=300

print(items)
print("dish" in items)
print("pizza" not in items)

del items["ice"]
print(items)
print(items["dish"])

print("---------------------------------------------------------------")

# コンテナの中のコンテナ（リストの中にリストを入れる）

lists=[]

sweets=["チョコ","スナック","せんべい"]
ices=["カップ型","コーン型","棒型"]
dishs=["唐揚げ","まぜそば","スパゲティ"]

lists.append(sweets)
lists.append(ices)
lists.append(dishs)

print(lists)
print(lists[2])
print(dishs[2])

dishs.append("pizza")
print(lists)
print(lists[2])
print(dishs)

print("---------------------------------------------------------------")

# リストの中にタプルを持たせる

la=(34.1,188.2)
chicago=(41.9,87.6)

locations=[la,chicago]
print(locations)

print("---------------------------------------------------------------")

# リストの要素に辞書を持たせる

items2={"ケーキ":500,"プリン":120}

item_lists=[items,items2]
print(item_lists)
print(item_lists[0])
