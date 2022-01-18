"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_customer/', views.add_customer),
    path('pending/', views.new_pending),
    path('finished/', views.add_finished),
    path('bought/', views.bought),
    path('stock/', views.get_stock),
    path('suppliers/', views.get_suppliers),
    path('workers/', views.add_worker),
    path('cars/', views.cars),
    path('works/', views.works),
    path('', views.landing),
    path('signin/', views.signin),
]
