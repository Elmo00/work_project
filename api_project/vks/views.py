from django.core.paginator import Paginator
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import EventsVKS
from .forms import EventsVKSForm

@login_required
def events(request, page=1, error=''):
    # Запрос к бд и вывод стрпаниц всех записей о мероприятиях
    all_event = EventsVKS.objects.all().reverse()
    paginator = Paginator(all_event, 15)
    event_paginator = paginator.page(page)
    context = {'events_vks': all_event, #не юзаю
               'events': event_paginator,
               'error': error}
    return render(request, 'vks/events.html', context)

@login_required
def add_event(request):
    # Заполнение формы, проверка на пост запрос и
    current_page = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            form = EventsVKSForm(request.POST)  # Проверяем заполенние формы
            # if form.is_valid():
            form.save()
            return HttpResponseRedirect(current_page)
        except ValueError:
            error = 'error переданы не верные данные'
            return events(request, error=error)
    else:
        return HttpResponseRedirect(current_page)
