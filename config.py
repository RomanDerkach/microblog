import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "standart-secret-key-1111"
