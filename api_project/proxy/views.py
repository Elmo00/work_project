from django.shortcuts import render, get_object_or_404
from .models import Department, DepartmentUser
from .request_to_db import connection


def division(request):
    #вывод всех структурных
    all_division = Department.objects.all()
    context = {'division': all_division}
    return render(request, 'proxy/index.html', context)


def department_users(request, id_department):
    # вывод всех пользователей структурного
    department = get_object_or_404(Department, id=id_department)
    department_user = DepartmentUser.objects\
        .filter(department_name=department)\
        .order_by('user_name')
    context = {
        'department': department,
        'department_user1': department_user,
    }
    return render(request, 'proxy/department_users.html', context)


def proxy_user(request, id_proxy_user):
    #инфа о юзвере
    user = get_object_or_404(DepartmentUser, id=id_proxy_user)
    if request.method == 'POST':
        print(request.POST.get('from_data'))
        print(request.POST.get('to_data'))
    # connection()
    context = {
        'user1': user,
    }
    return render(request, 'proxy/proxy_user.html', context)
