from flask import Blueprint, redirect, url_for

lab1 = Blueprint('lab1',__name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>НГТУ, ФБ, Лабораторные работы</title>
            <link rel="stylesheet" href=" """ + url_for('static', filename='main.css') + """ ">
        </head>
        <body>
            <header>
                НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
            </header>

            <li><a href="/lab1">Лабораторная работа 1</a></li>
            <li><a href="/lab2">Лабораторная работа 2</a></li>
            <li><a href="/lab3">Лабораторная работа 3</a></li>
            <li><a href="/lab4">Лабораторная работа 4</a></li>
            <li><a href="/lab5">Лабораторная работа 5</a></li>
            <li><a href="/lab6">Лабораторная работа 6</a></li>
            <li><a href="/lab7">Лабораторная работа 7</a></li>
            <li><a href="/lab11">Защита</a></li>
            <footer>
                &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
            </footer>
        </body>
    </html>
    """


@lab1.route("/lab1")
def lab():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title> Колесников Дмитрий Константинович, лабораторная 1</title>
            <link rel="stylesheet" href=" """ + url_for('static', filename='main.css') + """ ">
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>Web-сервер на flask</h1>
            <div>Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов

            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</div>
            <a style="margin-left: 48%;" href="/menu">Меню</a>
            <h1>Реализованные роуты</h1>
            <b>
            <a class="rout" href="/lab1/oak">Дуб</a><br>
            <a class="rout" href="/lab1/student">Студент</a><br>
            <a class="rout" href="/lab1/python">Python</a><br>
            <a class="rout" href="/lab1/legend">Фильм "Легенда"</a><br>
            </b>
            <footer>
                &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
            </footer>
        </body>
    </html>
    """


@lab1.route('/lab1/oak')
def oak():
    return'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Dub</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>Дуб</h1>
            <img src="''' + url_for('static', filename='oak.jpg') + '''">
            <footer>
                &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''


@lab1.route('/lab1/student')
def student():
    return'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Student</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>Колесников Дмитрий Константинович</h1>
            <img src="''' + url_for('static', filename='student.png') + '''">
            <footer>
                &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''


@lab1.route('/lab1/python')
def python():
    return'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Python</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>Немного про Python</h1>
            <div>Название языка не имеет ничего общего со змеями, он назван так в честь популярной 
            британской комедийной труппы Монти Пайтона из 1970ых. Гвидо является большим фанатом 
            «Летающего Цирка Монти Пайтона». Находясь в довольно мрачном настроении, он и назвал проект 
            «Python». Разве это не интересный факт о Python?</div>
            <img src="''' + url_for('static', filename='python.png') + '''">
            <footer>
                &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''


@lab1.route('/lab1/legend')
def legend():
    return'''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Legend</title>
            <link rel="stylesheet" href="''' + url_for('static', filename='main.css') + '''">
        </head>
        <body>
            <header>
                НГТУ, ФБ, Лабораторная работа 1
            </header>
            <h1>Фильм "Легенда"</h1>
            <div>Братья Крэй родились 24 октября 1933 в семье торговца золотым ломом. 
            Отец редко бывал дома, мальчики находились под присмотром матери и многочисленной родни. 
            В детстве они начали заниматься боксом и имели вполне приличные перспективы. 
            Но спортивной карьере помешало отсутствие дисциплины и криминальные наклонности.</div>
            <img style="width: 900px; margin-top: 30px;"src="''' + url_for('static', filename='legend.png') + '''">
            <footer>
                &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
            </footer>
        </body>
    </html>
    '''