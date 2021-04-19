# coding: utf-8

# План
# 1. Посчитать топ 25 пользователей в базе - Готово
# 2. Число выполненных задач в базе - Готово
# 3. Пятый по задачам - Готово
# 4. Выполнители (Сколько в базе пользователей, у которых число невыполненных задач меньше 20?) - Готово
# 5. Логин второго с конца по невыполненным (Отсортируем пользователей по числу невыполненных задач.
# Как зовут второго по количеству невыполненных задач пользователя? Напишите его логин) - Готово

from pprint import pprint

from django.core.management import BaseCommand
from tasks.models import User
from collections import Counter
import pandas as pd


class Command(BaseCommand):

    help = u"Display top-25 users and they tasks"

    def handle(self, *args, **options):
        all_users_with_all_tasks_counter = Counter()
        users_with_completed_tasks_counter = Counter()
        users_with_uncompleted_tasks_counter = Counter()
        all_users_with_all_tasks_list = []
        all_users_with_completed_tasks_list = []
        all_users_with_uncompleted_tasks_list = []
        unexecutors = []
        executors = []
        for u in User.objects.all():
            for t in u.tasks.all():
                all_users_with_all_tasks_counter[u] += 1
                if t.is_completed:
                    users_with_completed_tasks_counter[u, t] += 1
                else:
                    users_with_uncompleted_tasks_counter[u, t] += 1

        for user, tasks in all_users_with_all_tasks_counter.most_common():
            all_users_with_all_tasks_list.append(str(user) + ' ' + str(tasks))

        df = pd.DataFrame(all_users_with_all_tasks_list, columns=['user'])
        df[['user', 'tasks']] = df.user.str.split(' ', expand=True)

        df.sort_values(by='tasks', ascending=False, inplace=True)
        five_user = df.iloc[4]
        print('Top 25')
        print(df[:25])
        print('Completed tasks', len(users_with_completed_tasks_counter))
        print('Пятый по задачам\n', five_user)
        for user, tasks in users_with_completed_tasks_counter.elements():
            all_users_with_completed_tasks_list.append(str(user) + ',' + str(tasks))

        df = pd.DataFrame(all_users_with_completed_tasks_list, columns=['user'])
        df[['user', 'tasks']] = df.user.str.split(',', expand=True)
        my_dict = dict(df['user'].value_counts())
        for k, v in my_dict.items():
            if v < 20:
                executors.append(str(k) + ' ' + str(v))
        print('Выполнители:')
        for item in executors:
            print(item)

        for user, tasks in users_with_uncompleted_tasks_counter.elements():
            all_users_with_uncompleted_tasks_list.append(str(user) + ',' + str(tasks))

        df = pd.DataFrame(all_users_with_uncompleted_tasks_list, columns=['user'])
        df[['user', 'tasks']] = df.user.str.split(',', expand=True)
        my_dict = dict(df['user'].value_counts())
        for k, v in my_dict.items():
            unexecutors.append(str(k) + ' ' + str(v))
        print('2 с конца по не выполненым задачам:')
        print(unexecutors[-2])
