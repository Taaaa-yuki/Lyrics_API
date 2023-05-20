import os
from flask import Flask
from routes import scrape_route, catch_all

app = Flask(__name__)

app.register_blueprint(scrape_route)
app.register_blueprint(catch_all)


if __name__ == '__main__':
    def get_port():
        # 環境変数からポート番号を取得する関数
        return int(os.environ.get('PORT', 5000))

    def start_app():
        # アプリを起動する関数
        port = get_port()
        app.run(debug=True, port=port)

    start_app()
