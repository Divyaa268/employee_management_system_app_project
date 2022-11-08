from os import getcwd
from os.path import isfile

from django.test import TestCase
from django.test import SimpleTestCase


# Create your tests here.

# testing index function in views.py

class test_functions(SimpleTestCase):
    #Testing if Index.html Exists
    def test_index(self):
        assert isfile('emp_app/templates/index.html')
