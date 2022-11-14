from django.db import models, connection
from django.db.models import Manager


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'emp_app_department'


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'emp_app_role'


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    is_manager = models.CharField(max_length=100, default='N')

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.phone)

    class Meta:
        managed = True
        db_table = 'emp_app_employee'


class SingletonModel(models.Model):

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class CEO(SingletonModel):
    # This Uses Singleton Pattern as There can be only One CEO in a Company
    emp_id = models.IntegerField(null=False, primary_key=True)
    full_name = models.CharField(max_length=100, null=False)
    phone_number = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'emp_app_ceo'


class BestPerformers(Employee):
    # This Class Inherits from Employee Class
    award_title = models.CharField(max_length=100, null=False)
    date_awarded = models.DateField()

    class Meta:
        managed = True
        db_table = 'emp_app_bestperformers'

    def __str__(self):
        return "%s %s %s %s" % (self.first_name, self.last_name, self.award_title, self.date_awarded)
