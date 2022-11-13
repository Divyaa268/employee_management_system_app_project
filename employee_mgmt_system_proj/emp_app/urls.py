"""employee_mgmt_system_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
from django.contrib import admin
from django.urls import path, include
from . import views

# import employee_mgmt_system_proj.emp_app.views as views

urlpatterns = [
    path('', views.index, name='index'),  # Routing to index page, sits at the root link
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),#Routes to add_emp page, to add new employee data
    path('remove_emp', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path('filter_emp', views.filter_emp, name='filter_emp'),
    path('manager_of_company', views.manager_of_company, name='manager_of_company'),
    path('ceo_details', views.ceo_details, name='ceo_details'),
    path('regular_employee', views.regular_employee, name='regular_employee'),
    path('best_performers', views.best_performers, name='best_performers'),
]
