# randomモジュール中のrandint関数（２つの整数の間で乱数を生成）

import random
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))
print(random.randint(0,100))

print("---------------------------------------------------------------")

# statisticsモジュール中の関数　mean（平均値）,median（中央値）,mode（最頻値）

import statistics
nums=[1,3,5,7,9,11,13,11,89]

print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.mode(nums))

print("---------------------------------------------------------------")

# keywordモジュール中の関数　iskeyword　（ある文字列がpythonのキーワードかどうか確認）

import keyword
print(keyword.iskeyword("while"))
print(keyword.iskeyword("food"))

print("---------------------------------------------------------------")

# 作成した他のモジュールからインポート

import ipmodule
ipmodule.hello(":pypy")
print("。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。ー。")
