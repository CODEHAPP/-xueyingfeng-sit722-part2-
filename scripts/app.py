from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
@app.route('/books/')
def get_books():
    # 返回模拟书籍数据
    return 'List of books'

