from django.shortcuts import render, redirect
from .models import ContactUS, Partner, OurClient
from invitation_app.models import Event_Type
from .forms import ContactUsForm
from invitation_app.models import Event, Guest, City

# Create your views here.


def home(request):
    partners = Partner.objects.all()
    # num_event = Event.objects.all().count()
    # num_guest = Guest.objects.all().count()
    # num_city = City.objects.all().count()
    events = Event_Type.objects.all()
    clients = OurClient.objects.all()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('xdesign')

    else:
        form = ContactUsForm()

    context = {
        'form': form,
        'partners': partners,
        # 'num_event': num_event,
        # 'num_guest': num_guest,
        # 'num_city': num_city,
        'events': events,
        'clients': clients,
    }
    return render(request, 'landing/home.html', context)
