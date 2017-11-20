#!/bin/sh
venv/bin/celery -A tareas:app worker --loglevel=info
