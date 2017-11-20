# -*- coding: utf-8 -*-
import time

from celery import Celery

app = Celery('tareas', broker='redis://localhost/0')

@app.task
def sumar(x, y):
    return x + y

@app.task
def esperar():
	for x in range(5):
		print(x)
		time.sleep(1)
