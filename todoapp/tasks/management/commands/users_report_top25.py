# coding: utf-8

# План
# 1. Посчитать топ 25 пользователей в базе - Готово
# 2. Число выполненных задач в базе - Готово
# 3. Пятый по задачам - Готово
# 4. Выполнители (Сколько в базе пользователей, у которых число невыполненных задач меньше 20?)
# 5. Логин второго с конца по невыполненным (Отсортируем пользователей по числу невыполненных задач.
# Как зовут второго по количеству невыполненных задач пользователя? Напишите его логин)

from pprint import pprint

from django.core.management import BaseCommand
from tasks.models import User
from collections import Counter
import pandas as pd


class Command(BaseCommand):

    help = u"Display top-25 users and they tasks"

    def handle(self, *args, **options):
        users_raw = Counter()
        completed_tasks = Counter()
        uncompleted_tasks = Counter()
        users = []
        for u in User.objects.all():
            for t in u.tasks.all():
                users_raw[u] += 1
                if t.is_completed:
                    completed_tasks[t] += 1
                else:
                    uncompleted_tasks[t] += 1

        for user, tasks in users_raw.most_common():
            users.append(str(user) + ' ' + str(tasks))

        df = pd.DataFrame(users, columns=['user'])
        df[['user', 'tasks']] = df.user.str.split(' ', expand=True)

        df.sort_values(by='tasks', ascending=False, inplace=True)
        five_user = df.iloc[4]
        print('Top 25')
        print(df[:25])
        print('Completed tasks', len(completed_tasks))
        print('Пятый по задачам\n', five_user)
