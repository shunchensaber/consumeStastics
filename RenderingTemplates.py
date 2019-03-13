from flask import render_template, Flask
app = Flask(__name__)

#你可以使用 render_template() 方法来渲染模板。你需要做的一切就是将模板名和
# 你想作为关键字的参数传入模板的变量。这里有一个展示如何渲染模板的简例:


@app.route('/hello')
@app.route('/hello/<name>')
def show_hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/x/<int:i>')
def show_index(i):
    return "index是 %s" % i


if __name__ == '__main__':
    app.run()



