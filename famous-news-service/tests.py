import json
import unittest
from app import app
from flask_testing import TestCase

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('object.TestingConfig')
        return app
    
class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('object.TestingConfig')
        return app
    
    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is True)

class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('object.TestingConfig')
        return app
    
    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])

class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('object.ProductionConfig')
        return app
    
    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])

class TestNewsService(BaseTestCase):
    def test_add_news(self):
        """ ensure the new user can add new news to the databases """
        with self.client:
            response = self.client.post(
                '/famous/news',
                data=json.dumps(dict(
                    title='My Test',
                    content='Just a service test',
                    tabs=['Test', 'functional_test'],
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('My Test', data['news']['title'])

        if __name__ == '__main__':
            unittest.main()