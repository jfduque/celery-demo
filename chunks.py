# -*- coding: utf-8 -*-
from tareas import sumar

items = zip(xrange(20), range(1, 20))
print(items)
sumar.chunks(items, 10).apply_async()
