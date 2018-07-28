# src/tests/test_base.py

import os
import sys
import inspect
import unittest
import tempfile

from src.app import app, db

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'test_app.db')
db_url = 'sqlite:///' + db_path


class BasicTests(unittest.TestCase):
    """setUp and tearDown"""

    print('test')

    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = db_url
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        os.unlink(db_path)

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
