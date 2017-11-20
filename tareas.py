# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('tareas', broker='redis://localhost/0')

@app.task
def sumar(x, y):
    return x + y
    