# pip パッケージインストール方法（インストール先はsite-packagesディレクトリを使う）
# ※コマンドラインを「管理者権限」で起動する必要がある！！
# pipでインストールしたFlaskモジュールを使用する例

from flask import Flask

app=Flask(__name__)
@app.route("/")
def index():
    return "Hello,World!"

app.run(port=8000)