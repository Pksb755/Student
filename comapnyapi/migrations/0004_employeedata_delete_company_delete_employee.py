# Generated by Django 5.0.6 on 2024-06-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapi', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneno', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
                ('confirmpassword', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('degree', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'employeedata',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]