from flask import Blueprint, redirect, url_for, render_template

lab2 = Blueprint('lab2',__name__)


@lab2.route('/lab2/example')
def example():
    name, lab_namber, group, kurs = 'Колесников Дмитрий', 'Лабораторная работа 2', 'ФБИ-12', '3 курс'
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 120},
        {'name': 'Апельсины', 'price': 80},
        {'name': 'Мандарины', 'price': 95},
        {'name': 'Манго', 'price': 321}
        ]
    books = [
        {'autor': 'Маргарет Митчелл' , 'name_book': 'Унесенные ветром' , 'genre': 'Исторический роман' , 'pages': 992},
        {'autor': 'Стивен Кинг' , 'name_book': '11/22/63' , 'genre': ' Научная фантастика' , 'pages': 800},
        {'autor': 'Ной Гордон' , 'name_book': 'Лекарь. Ученик Авиценны' , 'genre': 'Исторические приключения' , 'pages': 816},
        {'autor': 'Джон Стейнбек' , 'name_book': 'К востоку от Эдема' , 'genre': 'Классическая проза' , 'pages': 768},
        {'autor': 'Джордж Элиот' , 'name_book': 'Мидлмарч' , 'genre': 'Зарубежная классика' , 'pages': 832},
        {'autor': 'Джордж Оруэлл' , 'name_book': '1984' , 'genre': 'Фантастика' , 'pages': 328},
        {'autor': 'Михаил Булгаков' , 'name_book': 'Мастер и Маргарита' , 'genre': 'Роман' , 'pages': 384},
        {'autor': 'Фёдор Достоевский' , 'name_book': 'Преступление и наказание' , 'genre': 'Роман' , 'pages': 560},
        {'autor': 'Дж. К. Роулинг' , 'name_book': 'Гарри Поттер и философский камень' , 'genre': 'Фэнтези' , 'pages': 309},
        {'autor': 'Антуан де Сент-Экзюпери' , 'name_book': 'Маленький принц' , 'genre': 'Философская притча' , 'pages': 96}
    ]
    return render_template('example.html', name=name, lab_namber=lab_namber, group=group, kurs=kurs, fruits=fruits, books=books)


@lab2.route('/lab2/')
def lab():
   return render_template('lab2.html')

@lab2.route('/lab2/hallucinogenic_plants/')
def hallucinogenic_plants():
    return render_template('hallucinogenic_plants.html')