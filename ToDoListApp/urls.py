"""ToDoListApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path
from django.views import static

urlpatterns = [
    path('', views.ToDoListApp, name="ToDoListApp"),
    path('today', views.today, name="today"),
    path('this_week', views.this_week, name='this_week'),
    path('this_month', views.this_month, name='this_month'),
    path('spare_time_tasks', views.spare_time_tasks, name='spare_time_tasks'),

    path('delete/<list_id>', views.delete, name='delete'),
    path('delete_today/<list_id>', views.delete_today, name='delete_today'),
    path('delete_thisweek/<list_id>', views.delete_thisweek, name='delete_thisweek'),
    path('delete_thismonth/<list_id>', views.delete_thismonth, name='delete_thismonth'),
    path('delete_spare_time/<list_id>', views.delete_spare_time, name='delete_spare_time'),

    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('cross_off_today/<list_id>', views.cross_off_today, name='cross_off_today'),
    path('cross_off_thisweek/<list_id>', views.cross_off_thisweek, name='cross_off_thisweek'),
    path('cross_off_thismonth/<list_id>', views.cross_off_thismonth, name='cross_off_thismonth'),
    path('cross_off_spare_time/<list_id>', views.cross_off_spare_time, name='cross_off_spare_time'),

    path('uncross/<list_id>', views.uncross, name='uncross'),
    path('uncross_today/<list_id>', views.uncross_today, name='uncross_today'),
    path('uncross_thisweek/<list_id>', views.uncross_thisweek, name='uncross_thisweek'),
    path('uncross_thismonth/<list_id>', views.uncross_thismonth, name='uncross_thismonth'),
    path('uncross_spare_time/<list_id>', views.uncross_spare_time, name='uncross_spare_time'),
]

