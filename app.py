from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def start():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <a href="/lab1">Лабораторная работа 1</a>
        
        <footer>
            &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title> Колесников Дмитрий Константинович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        <div>Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов

        веб-приложений, сознательно предоставляющих лишь самые ба-
        зовые возможности.</div>
        <footer>
            &copy: Колесников Дмитрий, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
