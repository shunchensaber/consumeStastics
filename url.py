from flask import Flask
from flask import url_for
from flask import request,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!' + '我是XXX'


@app.route('/text')
def page():
    return '这里是text的page'


@app.route('/user/<username>')
def show_user(username):
    return '欢迎你 %s' % username


@app.route('/pageindex/<int:index>')
def show_currentPage(index):
    return '当前的页码是 %d' % index

#用url_for构造url 未来可以一次性替换url而不用到处替换


@app.route('/url_for/')
def show_page(id):
    pass


with app.test_request_context():
    print(url_for('show_page', id=1))
    print(url_for('show_page', id=2, next='/'))

#Http方法


@app.route('login', methods=['GET', 'POST'])
def login():
    if request.method == 'post':
        do_the_login()
    else:
        show_the_login()


def do_the_login():
    return redirect('user/chen')


def show_the_login():
    return '正在提交'

