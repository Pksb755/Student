"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


# urls.py

# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeDataViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import EmployeeDataViewSet

# router = DefaultRouter()
# router.register(r'employees', EmployeeDataViewSet, basename='employee')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# from django.contrib import admin
# from django.urls import path, include
# from companyapi.views import CompanyViewSet
# from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'companies',CompanyViewSet)

# urlpatterns = [
#     path('',include(router.urls))
# ]
