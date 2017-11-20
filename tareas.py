# -*- coding: utf-8 -*-
import time
import requests

from lxml import html
from celery import Celery

app = Celery('tareas', broker='redis://localhost/0')

@app.task
def sumar(x, y):
    z = x + y
    print('%s + %s = %s' % (x, y, z))
    return z

@app.task
def esperar():
    for x in range(5):
        print(x)
        time.sleep(1)

@app.task
def trm():
    page = requests.get('http://portal.banrep.gov.co/newwap/cambiaria.htm')
    tree = html.fromstring(page.content)

    trm_value = tree.xpath('/html/body/div[3]/table/tr[2]/td[2]/text()')
    return trm_value
