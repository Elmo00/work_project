from django.contrib import admin
from .models import EventsVKS

class AdminEvent(admin.ModelAdmin):
    list_display = ('event_data', 'event_time', 'event_organizer',
                    'event_type', 'event_place', 'event_document',
                    'event_description')
    list_display_links = ('event_document',)
    search_fields = ('event_data', 'event_time', 'event_organizer')
    list_filter = ('event_data', 'event_time')
    list_editable = ('event_data', 'event_time')
    list_per_page = 10
    list_max_show_all = 100
    fields = (('event_data', 'event_time'), ('event_organizer', 'event_document'),
              ('event_type', 'event_place'), 'event_description')


admin.site.register(EventsVKS, AdminEvent)

# Register your models here.
