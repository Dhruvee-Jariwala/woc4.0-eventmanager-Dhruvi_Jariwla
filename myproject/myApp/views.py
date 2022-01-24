from django.shortcuts import render, HttpResponse
# this is how we will load the db tables in views
from myApp.models import Events

def eventRegistration(request):
    # from eventRegistration page/template some data will arrive and we have to pass it to model
    if request.method == "POST":
        name = request.POST.get('event_name')
        location = request.POST.get('event_location')
        desc = request.POST.get('event_desc')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        host_email = request.POST.get('host_email')
        host_pw = request.POST.get('host_pw')
        deadline_date = request.POST.get('deadline_date')

        # now we will make the object of the table row
        print("Event  : " + name + location + desc + from_date + to_date + host_email + host_pw + deadline_date)

        event = Events(name=name, location=location, desc=desc, from_date=from_date, to_date=to_date, host_email=host_email, host_pw=host_pw, deadline_date=deadline_date)
        event.save()
        print("Event name : "+event.name)
        print("Event location : " + event.location)

    return render(request, 'eventRegistration.html')

def eventList(request):
    data = {
        'events' : Events.objects.all()
    }
    return render(request, 'eventList.html',data)
# Create your views here.

def index(request):
    # return HttpResponse("This is myApp Index function")
    #now we will use render for templates
    # render will render the index.html when request is made. It will find index.html in the template dir just set in settings.py

    #we will send some data to the template
    # return render(request, 'index.html')
    return render(request, 'index.html')