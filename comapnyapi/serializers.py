# serializers.py

# serializers.py
import re
from rest_framework import serializers
from .models import EmployeeData

class EmployeeDataSerializer(serializers.HyperlinkedModelSerializer):
    # ConfirmPassword = serializers.CharField(write_only=False)

    class Meta:
        model = EmployeeData
        fields = '__all__'
        extra_kwargs = {
            'Firstname': {'required': True},
            'Lastname': {'required': True},
            'Email': {'required': True},
            'Phoneno': {'required': True},
            'Passwor': {'required': True},
            'ConfirmPassword': {'required': True},
            'Area': {'required': True},
            'PinCode': {'required': True},
            'DOB': {'required': True},
            'Gender': {'required': True},
            'Degree': {'required': True},
            'Addres': {'required': True},
        }

    # def validate(self, data):
    #     errors = {}

    #     # Validate Firstname
    #     if any(char.isdigit() for char in data.get('Firstname', '')):
    #         errors['Firstname'] = ["First name cannot contain numbers."]
    #     pattern = r'[0-9!@#$%^&*(),.?"`/:|<>\']'
    #     if re.search(pattern, data.get('Firstname', '')):
    #         errors['Firstname'] = ["First name cannot contain Special characters."]

    #     # Validate Email uniqueness
    #     if 'Email' in data:
    #         existing_employee = EmployeeData.objects.filter(Email=data['Email']).exists()
    #         if existing_employee:
    #             errors['Email'] = ["Employee data with this Email already exists."]

    #     # Validate Phoneno presence
    #     if 'Phoneno' not in data:
    #         errors['Phoneno'] = ["Phone number is required."]

    #     if errors:
    #         raise serializers.ValidationError(errors)

    #     return data

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['confirm_password'] = ""  # Exclude confirm_password from output
    #     return representation
    def to_representation(self, value):
        data = super().to_representation(value)
    
        return data
        

    def validate_Firstname(self, value):
        pattern = r'[0-9!@#$%^&*(),.?"`/:|<>\']'
        if re.search(pattern, value):
            raise serializers.ValidationError("First name cannot contain Special Characters.")
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("First name cannot contain numbers.")
        return value
            

    def validate_Lastname(self, value):
        pattern = r'[0-9!@#$%^&*(),.?":|<>]'
        if re.search(pattern, value):
            raise serializers.ValidationError("First name cannot contain Special Characters.")
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Last name cannot contain numbers.")
        return value


    def validate_PinCode(self, value):
        if len(value) != 6 or not value.isdigit():
            raise serializers.ValidationError("Pincode must be 6 digits long.")
        return value

    def validate_Phoneno(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("Phone number must be 10 digits long.")
        return value


    def validate_Email(self,value):
        pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]\b'
        if (re.fullmatch(pat,value)):
            raise serializers.ValidationError("Invalid Email Address.")
        return value

    def create(self, validated_data):
        if validated_data.get('Passwor') != validated_data.get('ConfirmPassword'):
            raise serializers.ValidationError({"ConfirmPassword": "Password and Confirm Password do not match."})
        return super().create(validated_data)


# from rest_framework import serializers
# from .models import EmployeeData

# class EmployeeDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeData
#         fields = '__all__'

# from rest_framework import serializers
# from companyapi.models import Company,Employee

# #Create Serializers
# class CompanySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=Company
#         fields="__all__"

# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Employee
#         fields = "__all__"