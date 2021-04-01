# coding: utf-8
from django.core.management import BaseCommand
from tasks.models import TodoItem
import os


class Command(BaseCommand):

    help = u"Read tasks from file (one line = one task) and save them to db"

    def add_arguments(self, parser):
        parser.add_argument('--file', dest='input_file', type=str)

    def handle(self, *args, **options):
        path = os.getcwd() + '/tasks/management/commands/'
        data = options['input_file']
        with open(os.path.join(path, data), 'r') as f:
            for row in f.readlines():
                desc = row.split(sep='\n')[0]
                t = TodoItem(description=desc)
                t.save()
