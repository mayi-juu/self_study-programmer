def hello(guest):
    print("hello"+guest)

print("ipmoduleをインポートしました。")

# インポートしたときに実行されないようにするためのコード（if __name__ == "__main__":）
if __name__=="__main__":
    hello(":python")
    print("。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。")
