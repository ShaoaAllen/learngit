from form import *
from flask import *
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'some_secret'

# 因不会连接数据库，所以只能把数据打印到控制台
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.username.data, form.password.data, form.email.data)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# 登录路由，把帐号密码写死成admin，123
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.username.data, form.password.data)
        if request.form['username'] == 'admin' and\
                request.form['password'] == '123':
            flash('You were successfully logged in')
            return redirect(url_for('user'))
        else:
            flash('Failed')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

# 想使url默认跳转到登录界面，所以重复写了一个登录路由
@app.route('/', methods=['POST', 'GET'])
def default():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.username.data, form.password.data)
        if request.form['username'] == 'admin' and\
                request.form['password'] == '123':
            flash('You were successfully logged in')
            return redirect(url_for('user'))
        else:
            flash('Failed')
            return redirect(url_for('login'))

    return render_template('login.html', form=form)

# 登录后的欢迎界面
@app.route('/user', methods=['POST', 'GET'])
def user():
    form = LoginForm(request.form)
    return render_template('user.html', form=form)


if __name__ == '__main__':
    app.run()
