from bottle import request, route, run, view
from datetime import datetime
from random import random
from horoscope import generate_prophecies
from my_logging import get_logger


logger = get_logger('divider-server')


def tell_me_your_secret():
    return 42


@route('/<top:int>/<bottom:int>')
def danger(top, bottom):
    res = {'result': 0, 'error': None}
    try:
        res['result'] = top / bottom
    except ZeroDivisionError as zd:
        res['error'] = f'Для входных данных {top} и {bottom} не получилось {zd}'
        agent = request.headers["User-Agent"]
        host = request.headers["Host"]
        path = request.path
        logger.error(f"Ошибка деления при обращении к {host}{path}. User-Agent: {agent}")
    return res
# def danger(top, bottom):
    # return {
    #     'result': top / bottom,
    #     'error': None,
    #     'secret': tell_me_your_secret(),
    # }


@view('predictions')
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


if __name__ == '__main__':
    print("[server] __name__ =", __name__)
    run(
        host='localhost',
        port=8080,
        autoreload=True
    )
