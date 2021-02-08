# coding: utf-8

from datetime import datetime
from horoscope import generate_prophecies


def generate_head(title):
    head = '<meta charset=utf-8>' + '<title>' + title + '</title>'
    return '<head>' + head + '</head>'


def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body += "<p>" + p + "</p>"
    return "<body>" + body + "</body>"


def generate_page(head, body):
    page = '<html>' + head + body + '</html>'
    return page


def save_page(title, header, paragraphs, output='html/index.html'):
    with open(output, 'w') as fp:
        page = generate_page(

            head=generate_head(title=title),
            body=generate_body(header=header, paragraphs=paragraphs)
        )
        print(page, file=fp)


today = datetime.now().date()
save_page(
    title="Гороскоп на сегодня",
    header="Что день " + str(today) + " готовит.",
    paragraphs=generate_prophecies(),
)
