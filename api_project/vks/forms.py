from django.forms import ModelForm  # импортируем формы джанго
from .models import EventsVKS


class EventsVKSForm(ModelForm):
    # параметры а атрибуты которые мы хотим разместить там
    class Meta:
        model = EventsVKS
        fields = ['event_data', 'event_time', 'event_organizer', 'event_type',
                  'event_place', 'event_document', 'event_description'
                  ]  # то что будет отображатся
