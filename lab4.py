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
    if request.method== 'GET':
        return render_template('holod.html')
    temper = request.form.get('temper')
    error= ''
    if temper == '':
       error = 'Не задана температура'
    else:
        if temper:
            temper = int(temper)
            if (temper> -13) and 0>temper:
                if (temper> -13) and (-8>temper):
                    snow = '✻✻✻'
                elif (temper>-9) and (-4>temper):
                    snow = '✻✻'
                elif (temper>-5) and (0> temper):
                    snow = '✻'
                return render_template('temper.html',temper=temper,snow=snow)
            
            if temper< -12:
                error='не удалось установить температуру — слишком низкое значение'
            if temper > -1:
                error='не удалось установить температуру — слишком высокое значение'
    return render_template('holod.html', error=error, temper=temper)
 
@lab4.route('/lab4/temper')
def temper():
    return render_template('temper.html')