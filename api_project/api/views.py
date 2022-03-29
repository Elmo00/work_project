from django.shortcuts import render
# from vks.models import EventsVKS

def index(request):
    context = {}
    return render(request, 'api/index.html', context)


# def events(request):
#     context = {'events_vks': EventsVKS.objects.all()}
#     return render(request, 'api/events.html', context)
