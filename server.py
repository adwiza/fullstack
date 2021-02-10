from bottle import route, run, view
from datetime import datetime
from random import random
from horoscope import generate_prophecies


@route('/')
@view('predictions')
def index():
    now = datetime.now()
    special_day = random()
    predictions = generate_prophecies() + generate_prophecies() + generate_prophecies()
    return {
        'date': f'0{now.day}-0{now.month}-{now.year}',
        'predictions': predictions,
        'special_date': special_day > 0.5,
        'special_day': special_day,
    }


@route('/api/test')
def api_test():
    return {
        'test_passed': True
    }


run(
    host='localhost',
    port=8080,
    autoreload=True
)
