import os
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password


class TryDjangoTutTest(TestCase):
    
    def test_secret_key_test(self):
        
        SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
        # self.assertNotEqual(SECRET_KEY, 'abc123')
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f'Weak secret key{e.messages}'
            self.fail(e)
