from bottle import route, run, view
from datetime import datetime
from random import random
from horoscope import generate_prophecies


@route('/')
@view('predictions2')
def index():
    now = datetime.now()
    special_day = random()
    predictions = generate_prophecies() + generate_prophecies()
    return {
        'date': f'{now.day}-0{now.month}-{now.year}',
        'predictions': predictions,
        'special_date': special_day > 0.5,
        'special_day': special_day,
    }


@route('/api/forecasts')
def api_forecasts():
    return {
        'predictions': generate_prophecies(),
    }


run(
    host='localhost',
    port=8080,
    autoreload=True
)
