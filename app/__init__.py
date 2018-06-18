from flask import Flask

app = Flask(__name__)

# bottom import to avoid circular imports
from app import routers
