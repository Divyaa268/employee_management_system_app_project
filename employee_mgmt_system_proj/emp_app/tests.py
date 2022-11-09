from os import getcwd
from os.path import isfile

from django.test import TestCase
from django.test import SimpleTestCase

from django.urls import reverse, resolve
from . import views


# Create your tests here.

# -------------------------------------------------------------------------------
# Testing if all the template files exist as expected

# testing index function in views.py

class test_templates_exist(SimpleTestCase):
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


# --------------------------------------------------------------------------------

#Testing Views
class test_urls(SimpleTestCase):
    def test_index_url_resolved(self):
        # for routing : path('', views.index, name='index')
        url = reverse('index')
        print("url is : " + url)#Returns '/' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func, views.index) #It should Route to this function

    def test_all_emp_url_resolved(self):
        # for routing : path('all_emp', views.all_emp, name='all_emp')
        url = reverse('all_emp')
        print("url is : " + url)#Returns '/all_emp' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func, views.all_emp) #It should Route to this function

    def test_add_emp_url_resolved(self):
        # for routing : path('add_emp', views.add_emp, name='add_emp')
        url = reverse('add_emp')
        print("url is : " + url)#Returns '/' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func,views.add_emp) #It should Route to this function

