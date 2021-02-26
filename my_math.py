# coding: utf-8
import logging
from my_logging import get_logger

logging = get_logger(__name__, level=logging.DEBUG)


def careful_division(x, y):
    logging.debug(f'Получены аргументы {x} и {y}')
    if y == 0 or x == 0:
        return 0
    else:
        return x / y
