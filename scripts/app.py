from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/books/')
def get_books():
    # 返回模拟书籍数据
    return 'List of books'
if __name__ == '__main__':
    # 打印所有注册的路由
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000)
