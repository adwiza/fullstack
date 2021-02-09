from bottle import route, run, view
from datetime import datetime
from random import random


@route('/')
@view('predictions')
def index():
    now = datetime.now()
    special_day = random()

    return {
        'date': f'0{now.day}-0{now.month}-{now.year}',
        'predictions': [
            'Днём ожидайте гостей из забытого прошлого.',
            'Утром ожидайте встреч со старыми знакомыми.',
            'Днём предостерегайтесь приятных перемен.',
        ],
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
