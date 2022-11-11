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

def remove_emp(request, emp_id = 0):
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
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


