"""
モジュール名をre.pyにすると、import reでreライブラリを参照にするのではなく、
re.pyファイル自体（自分自身）を見るようになってしまう！！⇒ファイル名変える！！
"""

# reライブラリ、findall関数　シンプルマッチ　※re.IGNORECASE：大文字小文字の違いを無視（第3引数）

import re

l="Beautiful is better than ugly"
match1=re.findall("Beautiful",l)
match2=re.findall("beautiful",l)
match3=re.findall("beautiful",l,re.IGNORECASE)

print(match1)
print(match2)
print(match3)

print("......................................................")

#行の先頭に一致する正規表現パターン（^）

import re

alones="""I feel that programimg is very interesting If i can make App alone.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!"""

alone=re.findall("If",alones,re.MULTILINE)
print(alone)

alone2=re.findall("^If",alones,re.MULTILINE)
print(alone2)

print("......................................................")

#行の終端に一致する正規表現パターン($)

import re

utas="""If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!"""

uta=re.findall("idea.",utas,re.MULTILINE)
print(uta)

uta2=re.findall("idea.",utas)
print(uta2)

uta3=re.findall("idea.$",utas)
print(uta3)

uta4=re.findall("idea.$",utas,re.MULTILINE)
print(uta4)

# 第3引数：re.MULTILINE　を指定しないと、複数行の文字列が「１つの文字列(行)の集まり」と見なされてしまう！！
# ⇒"idea.$"で行の終端であるthose!しか検索ヒットしなくなる！

print("......................................................")

# 複数文字との一致[]

import re

string="Two too"
m=re.findall("t[ow]o",string,re.IGNORECASE)
print(m)

print("......................................................")

# 数値との一致 "\d"←バックスラッシュ！！

line="123 hi 34 hello."
n=re.findall("\d",line)
print(n)

print("......................................................")

# 繰り返し（*）、貪欲（*）、非貪欲（*?）

import re

t1="_one_ _two_ _three_"
t2="_one__two__three_"
t3="_one_two_three_"

found0=re.findall("_.*_",t1)
found1=re.findall("_.*?_",t1)
found2=re.findall("_.*?_",t2)
found3=re.findall("_.*?_",t3)

print(found0)

for match in found1:
    print(match)

print(found2)
print(found3)

print("......................................................")

# エスケープ（\\）：特別な文字を本来の文字に一致させる（ただの文字として扱う）

import re

line="I love $"
m1=re.findall("$",line,re.IGNORECASE)
m2=re.findall(".$",line,re.IGNORECASE)
m3=re.findall("\\$",line,re.IGNORECASE)

print(m1)
print(m2)
print(m3)

print("......................................................")

# Mad Libsゲーム

import re

text="""私が今ハマっていることは_スキル_です。なぜならそれは私がいずれ人生を_名詞_に生きるための
手段の一つだからです。プログラミングを勉強して案件を達成できると_職関連_として手に職をつけることができ、
その報酬を_増やす_に回すことで自由を手に入れることができます。"""

def mad_libs(mls):
    hints=re.findall("_.*?_",mls)
    if hints is not None:
        for word in hints:
            q="{}を入力：".format(word)
            new=input(q)
            mls=mls.replace(word,new,1)
        print("\n")
        mls=mls.replace("\n","")
        print(mls)
    else:
        print("mls入力エラーです")

mad_libs(text)





