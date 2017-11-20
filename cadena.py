# -*- coding: utf-8 -*-
from celery import chain

from tareas import sumar

chain(sumar.s(1, 2), sumar.s(3)).apply_async()
