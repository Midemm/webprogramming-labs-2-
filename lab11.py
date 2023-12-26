from flask import Blueprint, redirect, url_for, render_template, request
import math 
lab11 = Blueprint('lab11',__name__)


@lab11.route('/lab11/')
def lab():
    return render_template('lab11.html')

def describe_number(num):
    if num > 0:
        if num % 2 == 0:
            return "положительное четное число"
        else:
            return "положительное нечетное число"
    elif num < 0:
        if num % 2 == 0:
            return "отрицательное четное число"
        else:
            return "отрицательное нечетное число"
    else:
        return "нулевое число"

@lab11.route('/lab11/zac4', methods=['GET', 'POST'])
def zac4():
    result = None

    if request.method == 'POST':
        try:
            user_input = int(request.form['number'])
            result = describe_number(user_input)
        except ValueError:
            result = "Пожалуйста, введите целое число."

    return render_template('zac4.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

def calculate_product(A, B):
    if A >= B:
        return "A должно быть меньше B"

    product = 1
    for number in range(A, B + 1):
        product *= number

    return product

@lab11.route('/lab11/zac5', methods=['GET', 'POST'])
def zac5():
    result = None

    if request.method == 'POST':
        try:
            A = int(request.form['A'])
            B = int(request.form['B'])
            result = calculate_product(A, B)
        except ValueError:
            result = "Пожалуйста, введите целые числа."

    return render_template('zac5.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

def calculate_expression(N):
    result = 0
    sign = 1 

    for i in range(1, N + 1):
        result += sign * (1 + i / 10)
        sign *= -1  

    return result

@lab11.route('/lab11/zac6', methods=['GET', 'POST'])
def zac6():
    result = None

    if request.method == 'POST':
        try:
            N = int(request.form['N'])
            result = calculate_expression(N)
        except ValueError:
            result = "Пожалуйста, введите целое число."

    return render_template('zac6.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

@lab11.route('/lab11/zac7')
def zac7():
    return render_template('zac7.html')