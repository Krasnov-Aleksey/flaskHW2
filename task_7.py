"""
Создать страницу, на которой будет форма для ввода числа
и кнопка "Отправить"
При нажатии на кнопку будет произведено
перенаправление на страницу с результатом, где будет
выведено введенное число и его квадрат.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = int(request.form.get('number'))
        res = number ** 2
        context = {
            'number': number,
            'res': res,
        }
        return render_template('res.html', **context)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
