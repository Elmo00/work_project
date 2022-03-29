from django.urls import path

from .views import division, department_users, proxy_user

app_name = 'proxy'

urlpatterns = [
    path('', division, name='division'),
    path('department-users/<int:id_department>', department_users, name='department_users'),
    path('proxy-user/<int:id_proxy_user>', proxy_user, name='proxy_user'),
    ]
