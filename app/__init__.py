from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# bottom import to avoid circular imports
from app import routers
