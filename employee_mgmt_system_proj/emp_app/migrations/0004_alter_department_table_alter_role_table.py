# Generated by Django 4.1.3 on 2022-11-12 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_alter_department_options_alter_role_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='department',
            table='emp_app_department',
        ),
        migrations.AlterModelTable(
            name='role',
            table='emp_app_role',
        ),
    ]
