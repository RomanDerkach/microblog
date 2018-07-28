"""Test base module contains the base testing"""

import os
import unittest

from src.app import app, db

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DBPATH = os.path.join(BASEDIR, 'test_app.db')
DBURL = 'sqlite:///' + DBPATH


class BasicTests(unittest.TestCase):
    """setUp and tearDown"""

    print('test')

    def setUp(self):
        app.config["SQLALCHEMY_DATABASE_URI"] = DBURL
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        os.unlink(DBPATH)

    def test_main_page(self):
        """Check the main page fuctionality"""
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
