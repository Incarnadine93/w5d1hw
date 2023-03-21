
from app import app

from flask import render_template


@app.route('/')
def homePage():
    teachers = [
        {
        'name': 'Brendan',
        'age': 456,
        'spec' : 'Vim'
        },
        {
        'name': 'Rachel',
        'age' : 342,
        'spec' : 'student relations'
        },
        {
        'name' : 'Brandt',
        'age' : 567,
        'spec': 'none'
        }
    ]
    fav_animal = 'Tiger'
    return render_template('index.html', teachers=teachers, f = fav_animal)

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/top_5')
def top_5():
    return render_template('top_5.html')

@app.route('/home')
def home():
    return render_template('home.html')