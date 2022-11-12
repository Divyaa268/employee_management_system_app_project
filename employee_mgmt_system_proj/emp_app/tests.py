from os import getcwd
from os.path import isfile

from django.test import TestCase
from django.test import SimpleTestCase, Client

from django.urls import reverse, resolve
from . import views
from . import models
import json


# Create your tests here.

# -------------------------------------------------------------------------------
# Testing if all the template files exist as expected

# testing index function in views.py

class test_templates_exist(SimpleTestCase):
    # Testing if Index.html Exists or Not
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

    def test_view_remove_emp(self):
        #Checks if the page to add employee exists
        file_name = 'emp_app/templates/remove_emp.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/remove_emp.html')

    def test_filter_emp(self):
        #Checks if the page to add employee exists
        file_name = 'emp_app/templates/filter_emp.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/filter_emp.html')

    def test_manager_of_company(self):
        #Checks if the page to add employee exists
        file_name = 'emp_app/templates/manager_of_company.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/manager_of_company.html')

    def test_reg_emp_of_company(self):
        #Checks if the page to add employee exists
        file_name = 'emp_app/templates/regular_employee.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/regular_employee.html')

    def test_ceo_of_company(self):
        # Checks if the page to add employee exists
        file_name = 'emp_app/templates/ceo_details.html'
        if not isfile(file_name):
            print("File " + file_name + " Does Not Exist, Test Case Failed")
        else:
            print("File Exists Test Case is Successful")

        assert isfile('emp_app/templates/ceo_details.html')



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


    def test_remove_emp_url_resolved(self):
        # for routing : path('remove_emp', views.remove_emp, name='remove_emp')
        url = reverse('remove_emp')
        print("url is : " + url)  # Returns '/' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func, views.remove_emp)  # It should Route to this function

    def test_filter_emp_url_resolved(self):
        # for routing : path('remove_emp', views.remove_emp, name='remove_emp')
        url = reverse('filter_emp')
        print("url is : " + url)  # Returns '/' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func, views.filter_emp)  # It should Route to this function

    def test_filter_reg_emp_url_resolved(self):

        # path('regular_employee', views.regular_employee, name='regular_employee'),
        url = reverse('regular_employee')
        print("url is : " + url)  # Returns '/' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func, views.regular_employee)# It should Route to this function

    def test_filter_manager_url_resolved(self):
        # path('manager_of_company', views.manager_of_company, name='manager_of_company'),
        url = reverse('manager_of_company')
        print("url is : " + url)  # Returns '/' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func, views.manager_of_company)  # It should Route to this function

    def test_filter_ceo_url_resolved(self):
        # path('ceo_details', views.ceo_details, name='ceo_details'),
        url = reverse('ceo_details')
        print("url is : " + url)  # Returns '/' : the Path we defined
        print(resolve(url))  # Printing what we get after resolving the URL, i.e. method to be called

        self.assertEquals(resolve(url).func, views.ceo_details)  # It should Route to this function

# --------------------------------------------------------

class TestViews(TestCase):
    #Testing Get All Employees
    def test_project_GET_all_emp(self):
        #Created new Object of Client
        client = Client()

        response = client.get(reverse('all_emp'))

        #Check if we got a OK Http Response
        self.assertEquals(response.status_code, 200)#200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'view_all_emp.html')

    def test_project_index(self):
        #Created new Object of Client
        client = Client()

        response = client.get(reverse('index'))

        #Check if we got a OK Http Response
        self.assertEquals(response.status_code, 200)#200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'index.html')


    def test_project_add_emp(self):
        #Created new Object of Client
        client = Client()

        response = client.get(reverse('add_emp'))

        #Check if we got an OK Http Response
        self.assertEquals(response.status_code, 200)#200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'add_emp.html')

    def test_project_remove_emp(self):
        # Created new Object of Client
        client = Client()

        response = client.get(reverse('remove_emp'))

        # Check if we got an OK Http Response
        self.assertEquals(response.status_code, 200)  # 200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'remove_emp.html')

    def test_project_filter_emp(self):
        # Created new Object of Client
        client = Client()

        response = client.get(reverse('filter_emp'))

        # Check if we got an OK Http Response
        self.assertEquals(response.status_code, 200)  # 200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'filter_emp.html')
    def test_project_manager(self):
        # Created new Object of Client
        client = Client()

        response = client.get(reverse('manager_of_company'))

        # Check if we got an OK Http Response
        self.assertEquals(response.status_code, 200)  # 200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'manager_of_company.html')
    def test_project_reg_emp(self):
        # Created new Object of Client
        client = Client()

        response = client.get(reverse('regular_employee'))

        # Check if we got an OK Http Response
        self.assertEquals(response.status_code, 200)  # 200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'regular_employee.html')


    def test_project_ceo(self):
        # Created new Object of Client
        client = Client()

        response = client.get(reverse('ceo_details'))

        # Check if we got an OK Http Response
        self.assertEquals(response.status_code, 200)  # 200 = http OK, we were able to access

        # Check if we loaded the Correct Template i.e. HTML page
        self.assertTemplateUsed(response, 'ceo_details.html')
# -------------------------------------------------------------------------------


