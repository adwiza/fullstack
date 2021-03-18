import re

# Check URL's
# url_pg = 'postgres://admin:oocooSh7@postgres.host:5432/my_db'
# url_sqlite = 'sqlite:///home/user/site_db.sqlite3'


def parse_db_url(db_link='sqlite:///home/user/site_db.sqlite3'):
    """
    Функция возвращает словарь с параметрами подключения к БД
    :param db_link:  URL подключения к БД
    :return: Возвращает словать с параметрами БД
    """
    pattern_url = r'^([a-z]+)'  # Get Db type
    pattern_pg = r'^([postgres]+):+\/\/([a-z]+):([a-zA-Z0-9]+)@(postgres).(.+?)(?=\.?):([0-9]{4})\/(.+)$'  # reg exp PG
    pattern_sqlite = r'^([a-z]+):\W{2}(\W[a-zA-Z]+\W[a-zA-Z]+)\W(\w*).([a-z]+\d)$'  # reg exp sqlite
    db_type = re.compile(pattern_url)
    url_type = re.match(db_type, db_link)

    if url_type[1] == 'postgres':

        templ_pg = re.compile(pattern_pg)
        list_pg = templ_pg.split(db_link)
        pg_dict = {
            'ENGINE': f'django.db.backends.' + list_pg[1] + f'_psycopg2',
            'USER': list_pg[2],
            'PASSWORD': list_pg[3],
            'HOST': f'{".".join(list_pg[4:6])}',
            'PORT': list_pg[6],
            'NAME': list_pg[7]
        }
        return pg_dict
    elif url_type[1] == 'sqlite':
        templ_sqlite = re.compile(pattern_sqlite)
        list_sqlite = templ_sqlite.split(db_link)
        sqlite_dict = {
            'ENGINE': f'django.db.backends.{list_sqlite[4]}',
            'NAME': f'{list_sqlite[2]}/{list_sqlite[3]}.{list_sqlite[4]}'
        }
        return sqlite_dict
    else:
        raise ValueError('Неизвестный тип БД')
