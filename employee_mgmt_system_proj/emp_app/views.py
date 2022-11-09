from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


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