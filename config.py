import os
import random, string

basedir = os.path.abspath(os.path.dirname(__file__))

if not os.path.isdir(os.path.join(basedir, 'static/uploads')):
    os.mkdir(os.path.join(basedir, 'static/uploads'))


def key():
    try:
        open(os.path.join(basedir, "key"), "r").read()
    except FileNotFoundError:
        with open(os.path.join(basedir, "key"), "w", encoding='utf-8') as f:
            f.write(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(24)))
    return open("key", "r").read()


class Config:
    PORT = 8000
    SECRET_KEY = key()
    CSRF_ENABLED = True
    MONGODB_SETTINGS = {'DB': "localhost:27017"}
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']

class DevelopmentConfig(Config):
    DEBUG = True
