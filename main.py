from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def hi():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return 'Человечество вырастает из детства.<br>Человечеству мала одна ' + \
           'планета.<br>Мы сделаем обитаемыми безжизненные пока планеты.<b' + \
           'r>И начнем с Марса!<br>Присоединяйся!'


@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась"><br>\
           <div class="alert alert-primary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-dark" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      И тд...
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selecting', methods=['POST', 'GET'])
def astronaut_selecting():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="lastname" class="form-control" id="lastname" placeholder="Введите фамилию" name="lastname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <div class="form-group">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="obr" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее полное</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                        
                                        <div class="form-group">
                                        <label for="form-check">Какими профессиями вы владеете?</label>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="p1" name="p1">
                                        <label class="form-check-label" for="p1">Инженер-исследователь</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="p2" name="p2">
                                        <label class="form-check-label" for="p2">Инженер-строитель</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="p3" name="p3">
                                        <label class="form-check-label" for="p3">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="p4" name="p4">
                                        <label class="form-check-label" for="p4">Метеоролог</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="p5" name="p5">
                                        <label class="form-check-label" for="p5">Инженер по жизнеобеспечению</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="p6" name="p6">
                                        <label class="form-check-label" for="p6">Зоолог</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="p7" name="p7">
                                        <label class="form-check-label" for="p7">Врач</label>
                                        </div>
                                        <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="p8" name="p8">
                                        <label class="form-check-label" for="p8">Экзобиолог</label>
                                    </div>
                                    </div>
                                        
                                        <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите учавствовать в экспедиции?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div> 
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['lastname'])
        print(request.form['name'])
        print(request.form['class'])
        print(request.form['sex'])
        print(request.form.get('p1'))
        print(request.form.get('p2'))
        print(request.form.get('p3'))
        print(request.form.get('p4'))
        print(request.form.get('p5'))
        print(request.form.get('p6'))
        print(request.form.get('p7'))
        print(request.form.get('p8'))
        print(request.form['about'])
        f = request.files.get('file')
        print(f.read())
        print(request.form.get('accept'))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
