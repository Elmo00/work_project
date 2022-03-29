from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=200, verbose_name='Структурное подразделение')

    class Meta:
        verbose_name = 'Структурное подразделение'
        verbose_name_plural = 'Структурные подразделения'

    def __str__(self):
        return f'{self.department_name}'


class DepartmentUser(models.Model):
    user_name = models.CharField(max_length=100, verbose_name='ФИО')
    windows_name = models.CharField(max_length=100, blank=True, verbose_name='Логин домена')
    proxy_name = models.CharField(max_length=100, verbose_name='Логин прокси')
    post_name = models.CharField(max_length=200, blank=True, verbose_name='Должность')
    department_name = models.ForeignKey(Department, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Пользователь интернета'
        verbose_name_plural = 'Пользователи интернета'

    def __str__(self):
        return f'{self.user_name} | {self.post_name}'
