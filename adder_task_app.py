# Consumer
from celery import Celery
from celery_conf import celeryconfig

app = Celery()
app.config_from_object(celeryconfig,)


@app.task
def adder(x, y):
    import time
    time.sleep(10)
    return "type2"
