from os import getcwd
from os.path import isfile

from django.test import TestCase
from django.test import SimpleTestCase


# Create your tests here.

# testing index function in views.py

class test_functions(SimpleTestCase):
    # Testing if Index.html Exists
    def test_index(self):
        file_name = 'emp_app/templates/index.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/index.html')

    def test_add_emp(self):
        #Checks if the page to add employee exists
        file_name = 'emp_app/templates/index.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/index.html')

    def test_view_all_emp(self):
        #Checks if the page to add employee exists
        file_name = 'emp_app/templates/view_all_emp.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/index.html')