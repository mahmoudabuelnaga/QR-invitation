from django.shortcuts import render, redirect
from .models import About, Vision, ContactUS
from .forms import ContactUsForm

# Create your views here.


def home(request):
    about = About.objects.last()
    vision = Vision.objects.last()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('xdesign')

    else:
        form = ContactUsForm()

    context = {
        'about': about,
        'vision': vision,
        'form': form,
    }
    return render(request, 'landing/home.html', context)
