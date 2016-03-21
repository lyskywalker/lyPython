# coding=utf-8
from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from wtforms import Form, TextField, PasswordField, validators
from model import *
# from db import *
myapp = Flask(__name__)

myapp.debug = True                                   # 开启调试模式，方便定位错误
class loginForm(Form):
    username = TextField("username", [validators.Required()])
    password = PasswordField("password", [validators.required()])
class PublishForm(Form):
    content=TextField("content",[validators.Required()])
    sender=TextField("sender",[validators.Required()])

# @app.route('/', methods=['GET', 'POST'])
# def index():
# return redirect(url_for('hello'))


@myapp.route('/user', methods=['GET', 'POST'])
# def hello():
#
#
# if request.method == 'POST':
# # messag="backend message"
#         a = request.form['adder1']
#         b = request.form['adder2']
#         a = int(a)
#         b = int(b)
#         c = a % b
#         return render_template('add.html', message=str(c))
#     else:
#         return render_template('add.html')


def login():
    myForm = loginForm(request.form)
    if request.method == 'POST':
        # username = request.form['username']
        # password = request.form['password']
        u=Users(myForm.username.data,myForm.password.data)
        if u.isExisted():
            return redirect("http://www.baidu.com")
        else:
            error = "Login failed"
            return render_template('index.html', message=error, form=myForm)
    else:
        return render_template('index.html', form=myForm)


@myapp.route("/register", methods=['GET', 'POST']) # 注册页面路由
def register():

    myForm = loginForm(request.form)              # 实例化一个表单
    if request.method == 'POST':
        u=Users(myForm.username.data, myForm.password.data)
        u.add()
        return 'Register Successfully!'
    else:
        return render_template('index.html', form=myForm)
@myapp.route('/show',methods=['GET','POST'])
def show():
    myEntryForm=PublishForm(request.form)
    l=getAllEntry()
    if request.method=='POST':
        e=Entry(myEntryForm.content.data,myEntryForm.sender.data)
        e.add()
        l=getAllEntry()
        return render_template("show.html",entries=l,form=myEntryForm)
    return render_template("show.html",entries=l,form=myEntryForm)
# def index():
#     return render_template('video.html')
if __name__ == "__main__":
    myapp.run(port=8080)
