from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/book/<string:book_id>')
def book(book_id):
    return 'book_id:{}'.format(book_id)


@app.route('/stu/<string:stu_id>')
def stu(stu_id):
    return 'stu_id:{}'.format(stu_id)


if __name__ == '__main__':
    app.run()
