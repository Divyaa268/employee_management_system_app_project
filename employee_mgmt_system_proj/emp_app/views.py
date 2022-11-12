from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
from django.db import connection


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_emp(request):
    print("add_emp() routine started.....")
    # we will reach below code when we need to add new employee
    if request.method == 'POST':
        print("Request Method is POST")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])

        print("Creating New Entry to save in the DB.....")
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                           dept_id=dept, role_id=role, hire_date=datetime.now())
        print("Saving Entry in the DB.....")
        new_emp.save()
        print("Entry Added Successfully...")
        return HttpResponse('New Entity added Successfully')
    elif request.method == 'GET':
        print("GET Method Initiated....Stay on Same Page...")
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Entity could not be added!!!")


def all_emp(request):
    print("inside routine all_emp()")

    print("View All Employee Data")

    print("Fetching all Employees from DB.....")
    emps = Employee.objects.all()
    print("Data Fetched Successfully....")

    print("Loading Data into Context, for it to be rendered on the webpage")
    context = {
        'emps': emps
    }
    print(context)
    print("Data Loaded into context successfully....")
    print("Returning the rendered Page...")
    return render(request, 'view_all_emp.html', context)


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()

        print("Employees are :")
        print(emps)
        if name:
            pass
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            pass
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            pass
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


def manager_of_company(request):
    cursor = connection.cursor()
    # Example of Parameterised Query as Expected in the Project
    parameter_is_manager = 'Y'  # Indicates that Employee is a Manager
    try:
        cursor.execute(
            "SELECT first_name, last_name, phone FROM emp_app_employee where is_manager = " + "\'" + parameter_is_manager + "\'")
    except:
        print("Exception Occurred in manager_of_company() ")
    finally:
        query = cursor.fetchall()
        cursor.close()
    print("Manager Records are : ")
    print(query)
    return render(request, 'manager_of_company.html', {'query': query})

def ceo_details(request):

    cursor = connection.cursor()
    try:
        #Since CEO is a singleton class, the table emp_app_ceo has only one entry
        cursor.execute('select * from emp_app_ceo')
    except:
        print("Exception Occurred in get_ceo_details()")
    finally:
        query = cursor.fetchall()
        cursor.close()
        print("CEO of the Company is ")
        print(query)

        return render(request, 'ceo_details.html', {'query': query})




