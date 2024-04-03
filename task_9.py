"""
Создать страницу, на которой будет форма для ввода имени
и электронной почты
При отправке которой будет создан cookie файл с данными
пользователя
Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка "Выйти"
При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.

"""

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = '123'


@app.route('/', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        session['name'] = request.form.get('name')
        return redirect(url_for('hello', name=name))
    return render_template('index1.html')


@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name):
    if request.method == 'POST':
        session.pop('name', None)
        return redirect(url_for('index1'))
    context = {'name': name}
    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run()
