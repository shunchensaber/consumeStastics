from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask import Flask,render_template

#使用Wtf实现表单
#自定义表单类


class Loginform(FlaskForm):
    username = StringField('用户名')
    password = PasswordField('密码')
    password1 = PasswordField('确认密码')
    submit = SubmitField('提交')


app = Flask(__name__)
app.secret_key = 'aaaaaa'


@app.route('/')
def login():
    loginform = Loginform()
    return render_template('Login.html', loginform=loginform)


if __name__ == '__main__':
    app.run()









