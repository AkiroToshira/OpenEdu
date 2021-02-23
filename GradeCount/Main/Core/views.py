from flask import Blueprint, render_template, send_file

from jinja2 import Environment, FileSystemLoader

import requests

import json

import pdfkit

core = Blueprint('core', __name__)


@core.route('/simple/<int:pk>', methods=['GET'])
def user_register(pk):
    users = []
    url = "http://127.0.0.1:8000/gradecount/simple/{}".format(str(pk))
    res = requests.get(url)
    res = json.loads(res.text)
    for i in res['columns']:
        for j in i['grades']:
            check = False
            for k in users:
                if k['id'] == j['user']['id']:
                    try:
                        tmp_grade = int(k['grade']) + int(j['value'])
                        k['grade'] = tmp_grade
                    except:
                        pass
                    check = True
            if check:
                continue
            else:
                name = "{} {}. {}.".format(j['user']['last_name'], j['user']['first_name'], j['user']['middle_name'])
                if j['value'] == 'н':
                    users.append(dict(grade='0', name=name, id=j['user']['id'], exam='0',
                                      credit_book_number=j['user']['credit_book_number'], sum=0))
                else:
                    users.append(dict(grade=j['value'], name=name, id=j['user']['id'], exam='0',
                                      credit_book_number=j['user']['credit_book_number'], sum=0))
    for i in res['exam']:
        for k in users:
            if k['id'] == i['user']:
                k['exam'] = i['mark']
                if k['exam'] == '':
                    k['sum'] = int(k['grade'])
                else:
                    k['sum'] = int(k['exam']) + int(k['grade'])
                if 50 <= k['sum'] < 71:
                    k['text_grade'] = 'Три'
                elif 71 <= k['sum'] < 88:
                    k['text_grade'] = 'Чотири'
                elif 88 <= k['sum'] <= 100:
                    k['text_grade'] = 'П`ять'
                else:
                    k['text_grade'] = 'н/а'

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    wkhtmltopdf_options = {
        'enable-local-file-access': None,
        'page-size': 'A4',
        'margin-top': '0',
        'margin-right': '0',
        'margin-left': '0',
        'margin-bottom': '0',
        'zoom': '1.2',
        'encoding': "UTF-8",
    }
    lesson_info = res['lesson']
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    file_loader = FileSystemLoader('./Main/Core/templates')
    env = Environment(loader=file_loader)
    template = env.get_template('index.html')
    output = template.render(users=users, lesson=lesson_info)
    pdfkit.from_string(str(output), 'out.pdf', configuration=config, options=wkhtmltopdf_options)
    return send_file('..\out.pdf', attachment_filename='out.pdf')
