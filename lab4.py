from flask import Blueprint, render_template, request
import math 
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    errors={}
    if request.method == 'GET':
        return render_template('login.html', errors=errors)
    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('successs.html',username=username)
    
    errors["cred"]= 'Неверные логин и/или пароль'
    username= request.args.get('username')
    if username == '':
        errors['username']= 'Не введен логин!'
    if password == '':
        errors['password']= 'Не введен пароль!'
    return render_template('login.html', username=username, password=password, errors=errors)

@lab4.route('/lab4/successs')
def order():
    return render_template('login.html')

@lab4.route('/lab4/holod', methods = ['GET','POST'])
def holod():
    if request.method == 'GET':
        return render_template('holod.html')
    temper = request.form.get('temper')
    error= ''
    if temper == '':
       error = 'Не задана температура'
    else:
        if temper:
            temper = int(temper)
            if (temper > -13) and 0 > temper:
                if (temper > -13) and (-8 > temper):
                    snow = '✻✻✻'
                elif (temper > -9) and (-4 > temper):
                    snow = '✻✻'
                elif (temper > -5) and (0 > temper):
                    snow = '✻'
                return render_template('temper.html',temper=temper,snow=snow)
            
            if temper < -12:
                error='не удалось установить температуру — слишком низкое значение'
            if temper > -1:
                error='не удалось установить температуру — слишком высокое значение'
    return render_template('holod.html', error=error, temper=temper)
 
@lab4.route('/lab4/temper')
def temper():
    return render_template('temper.html')

@lab4.route('/lab4/zerno',methods = ['GET', 'POST'] )
def zerno():
    if request.method =='GET':
        return render_template('zerno.html')
    grain=request.form.get('grain')
    weight=request.form.get('weight')
    error=''
    if weight=='':
        error='Не ввели вес'
    else:
        weight=int(weight)
        if weight>50:
            sale=0.9
            message='Применена скидка за большой объем'
        else:
            sale=1
            message=''
    if grain =='ячмень':
        price= 12000*weight*sale
    elif grain=='овёс':
        price= 8500*weight*sale
    elif grain=='пшеница':
        price=8700*weight*sale
    else:
        price=14000*weight*sale
    if (weight>0) and (501>weight):
        return render_template('formzerno.html',grain=grain, weight=weight,
                                   price=price, message=message)
    if (weight<0) or weight==0:
        error = 'Неверное значение веса'
    elif weight> 500:
        error = 'Объем отстутствует в магазине'
    return render_template('zerno.html', grain=grain, weight=weight, error=error)
 
 
@lab4.route('/lab4/formzerno')
def formazerna():
    return render_template('formzerno.html')


@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')

    color = request.form.get('color')
    background = request.form.get('background')
    text = request.form.get('text')

    if color == request.cookies.get('background'):
        return 'Цвет текста не должен совпадать с цветом фона'

    try:
        text_size = int(text)
        if not (5 <= text_size <= 30):
            return 'Размер текста должен быть от 5px до 30px'
    except ValueError:
        return 'Некорректный размер текста'

    headers = {
      'Set-Cookie': f'color={color}; background={background}; path=/',
      'Location': '/lab4/cookies'
    }
    return '', 303, headers
