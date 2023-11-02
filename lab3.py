from flask import Blueprint, redirect, url_for, render_template, request
import math 
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1/')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('/form1.html', user=user, sex=sex, age=age, errors=errors)


@lab3.route('/lab3/order/')
def order():
    return render_template('/order.html')


@lab3.route('/lab3/pay/')
def pay():
    price=0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('/pay.html', price=price)


@lab3.route('/lab3/success/')
def success():
    return render_template('/success.html')


@lab3.route('/lab3/form2/')
def form2():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
        
    bilet_type = request.args.get('bilet_type')

    mesto = request.args.get('mesto')

    bagazh = request.args.get('bagazh')

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    Punkt_A = request.args.get('Punkt_A')
    if Punkt_A == '':
        errors['Punkt_A'] = 'Заполните поле!'

    Punkt_B = request.args.get('Punkt_B')
    if Punkt_B == '':
        errors['Punkt_B'] = 'Заполните поле!'

    data = request.args.get('data')
    if data == ' - - ':
        errors['data'] = 'Заполните поле!'
    return render_template('/form2.html', user=user, bilet_type=bilet_type, 
    mesto=mesto, bagazh=bagazh, age=age, Punkt_A=Punkt_A, Punkt_B=Punkt_B, data=data, errors=errors)


@lab3.route('/lab3/forthree/')
def forthree():
    x = request.args.get('x')
    n = request.args.get('n')

    result = 0
    if n and x:
        if int(n) > 0:
            n = int(n)
            x = float(x)

            result = x

            for i in range(n):
                result += (((-1**i)*(x**(2*i+1)))/(math.factorial(2*i+1)))
        else:
            result = 'error'
    
    return render_template('forthree.html', x=x, n=n, result=result)


@lab3.route('/lab3/lfnine/')
def lfnine():
    a = request.args.get('a')
    b = request.args.get('b')
    c = request.args.get('c')
    d = request.args.get('d')
    
    result = 0
    if a and b and c and d:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        if a == b == c:
            result = 4
        elif a == b == d:
            reuslt = 3
        elif a == c == d:
            result = 2
        else:
            result = 1
    return render_template('lfnine.html', a=a, b=b, c=c, d=d, result=result)