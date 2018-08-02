from src.app import app, db
from src.models import User, Post

app.run()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
