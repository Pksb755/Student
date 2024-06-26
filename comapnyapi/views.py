# views.py

# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import EmployeeData
from .serializers import EmployeeDataSerializer

class EmployeeDataViewSet(viewsets.ModelViewSet):
    queryset = EmployeeData.objects.all()
    serializer_class = EmployeeDataSerializer

    def __str__(self):
        return Response({"message": "Data Fetched successfully."}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        return Response({
            "status": 200,
            "message": "Employee list fetched successfully",
            "data": data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            error_messages = []
            for field, messages in e.detail.items():
                for message in messages:
                    error_messages.append(f"{field.replace('_', ' ').title()} {message}")

            error_message = ' and '.join(error_messages)
            return Response({
                "status": 422,
                "message": error_message
            }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "status": 201,
            "message": "Employee created successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "status": 200,
            "message": "Data updated successfully",
            "data": serializer.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status": 200,
            "message": "Data deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
    



# from rest_framework import viewsets
# from .models import EmployeeData
# from .serializers import EmployeeDataSerializer

# class EmployeeDataViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = EmployeeData.objects.all()
#     serializer_class = EmployeeDataSerializer

# # models.py

# from django.db import models

# class EmployeeData(models.Model):
#     id = models.AutoField(primary_key=True)
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phoneno = models.CharField(max_length=15)
#     password = models.CharField(max_length=100)
#     confirmpassword = models.CharField(max_length=100)
#     area = models.CharField(max_length=255)
#     pincode = models.CharField(max_length=10)
#     dob = models.DateField()
#     gender = models.CharField(max_length=10)
#     degree = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)
#     created_at = models.DateTimeField()

#     class Meta:
#         managed = False  # Do not create or modify the table, use the existing one
#         db_table = 'employeedata'  # Explicitly specify the table name

#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"

# # from django.shortcuts import render
# # from rest_framework import viewsets
# # from companyapi.models import Company,Employee
# # from companyapi.serializers import CompanySerializer,EmployeeSerializer

# # class CompanyViewSet(viewsets.ModelViewSet):
# #     queryset = Company.objects.all()
# #     serializer_class=CompanySerializer 

# # class EmployeeViewSet(viewsets.ModelViewSet):
# #     queryset = Employee.objects.all()
# #     serializer_class=EmployeeSerializer 
