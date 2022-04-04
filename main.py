from flask import Flask, render_template
from loginform import LoginForm
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_strong_secret_key'


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница', username=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/muraway.db")
    app.run(port=8080, host='127.0.0.1')
