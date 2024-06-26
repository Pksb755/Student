# models.py

from django.db import models

class EmployeeData(models.Model):
    id = models.AutoField(primary_key=True)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phoneno = models.CharField(max_length=15)
    Passwor = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=100)
    Area = models.CharField(max_length=255,choices=(('Bikaner','bikaner'),
                                                     ('Nokha','nokha'),
                                                     ('Deshnokh','deshnokh')))
    PinCode = models.CharField(max_length=10)
    DOB = models.DateField()
    Gender = models.CharField(max_length=10,choices=((('Male','male'),
                                                     ('Female','female'))))

    Degree = models.CharField(max_length=100,choices=((('BCA','bca'),
                                                     ('B.Tech','b.tech'),
                                                     ('M.Tech','m.tech'))))
    Addres = models.CharField(max_length=255)
    #created_at = models.DateTimeField()

    class Meta:
        managed = False  # Do not create or modify the table, use the existing one
        db_table = 'employeedata'  # Explicitly specify the table name

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

# from django.db import models
# # Create your models here.


# #Create Company model
# class Company(models.Model):
#     company_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     location = models.CharField(max_length=50)
#     about = models.TextField()
#     type = models.CharField(max_length=100,choices=(('IT','IT'),
#                                                     ('Non IT','Non IT'),
#                                                     ('Mobile Phones','Mobile Phones')))
#     added_date = models.DateTimeField(auto_now=True)
#     active=models.BooleanField(default=True)

# #employee Model
# class Employee(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.CharField(max_length=50)
#     address=models.CharField(max_length=200)
#     phone=models.CharField(max_length=10)
#     about=models.TextField()
#     position=models.CharField(max_length=100,choices=(('Manager','manager'),
#                                                     ('Software Developer','sd'),
#                                                     ('Project Leader','pj')))

# company = models.ForeignKey(Company,on_delete=models.CASCADE)