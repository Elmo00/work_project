from django.urls import path

from .views import events, add_event

app_name = 'vks'

urlpatterns = [
    path('', events, name='events'),
    path('add-event/', add_event, name='add_event'),
    path('page/<int:page>/', events, name='page'), #пагинация
    # path('', events, name='events'),
    ]
