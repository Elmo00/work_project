from django.db import models


class EventsVKS(models.Model):
    event_data = models.DateField(verbose_name='Дата')
    event_time = models.TimeField(verbose_name='Время')
    event_organizer = models.CharField(max_length=200, blank=True, verbose_name='Организатор')
    event_type = models.CharField(max_length=200, blank=True, verbose_name='Тип')
    event_place = models.CharField(max_length=200, blank=True, verbose_name='Зал')
    event_document = models.CharField(max_length=200, blank=True, verbose_name='Номер документа')
    event_description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        ordering = ['event_data', 'event_time']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return f'{self.event_data} | {self.event_type} | {self.event_place}'
