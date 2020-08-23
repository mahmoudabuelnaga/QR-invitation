import ast
import copy
import mimetypes
import os
import uuid
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from zipfile import ZipFile
from wsgiref.util import FileWrapper
from xml.dom import minidom
import simplejson
import json
from bootstrap_modal_forms.generic import BSModalReadView, BSModalDeleteView, BSModalCreateView, BSModalUpdateView
from django.core.files.base import ContentFile
from django.db.models import Count
from django.http import HttpResponse, HttpResponseServerError, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset
from .forms import FileUploadForm, EventsForms, GuestPopupForm
from .models import Event, Guest, City
import base64
from .resources import GuestResource
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('user_login'))


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('events'))
#             else:
#                 return render(request, 'login.html', {'message': 'Your account was inactive'})
#         else:
#             return render(request, 'login.html', {'message': 'Invalid login details given'})
#     else:
#         return render(request, 'login.html', {})


# def signup(request):
# if request.method == 'POST':
# form = UserCreationForm(request.POST)
# if form.is_valid():
# form.save()
# username = form.cleaned_data.get('username')
# raw_password = form.cleaned_data.get('password1')
# user = authenticate(username=username, password=raw_password)
# login(request, user)
# create_startup_event()
# return redirect('events')
# else:
# username = request.POST.get('username')
# email = request.POST.get('email')
# password1 = request.POST.get('password1')
# password2 = request.POST.get('password1')
# return render(request, 'registration/signup.html', {'form': form, 'username': username, 'email': email,
# 'password1': password1, 'password2': password2})
# else:
# form = UserCreationForm()
# return render(request, 'registration/signup.html', {'form': form})


@login_required
def design(request, event_id):
    openImageDialog = 'true'
    event = Event.objects.get(id=event_id, user_id=request.user)
    file_path = 'media/' + str(event.svg)
    doc = minidom.parse(file_path)
    for path in doc.getElementsByTagName('path'):
        event_svg_d_path = path.getAttribute('d')
    if event.image or event.image_state:
        openImageDialog = 'false'
    return render(request, 'invitation/design.html', {'event_id': event_id, 'openImageDialog': openImageDialog,
                                                      'svgPath': str(event_svg_d_path)})


def create_startup_event():

    newevent = Event(event_name='Start up Design')
    newevent.save()
    event = Event.objects.get(pk=newevent.id)
    file_path = 'media/startup_event/startup_design_state.json'
    with open(file_path) as f:
        json_data = json.load(f)
    json_values = simplejson.dumps(json_data)
    event.image_state.save('state_for_event_id_' +
                           str(event.id) + '.json', ContentFile(json_values))
    uid = uuid.uuid4()
    img_data = open('media/startup_event/startup_design_image.png', 'rb')
    event.image.save('image_for_event_id_' + str(event.id) +
                     '_' + str(uid) + '.' + 'png', img_data)


@csrf_exempt
def convert_data_to_image(request, event_id):
    json_values = simplejson.dumps(request.body)  # convert to json values
    string_values = json.loads(json_values)  # convert to string
    dictionary_values = ast.literal_eval(
        string_values)  # convert to dictionary
    format, imgstr = dictionary_values['data'].split(';base64,')
    ext = format.split('/')[-1]
    data_image = ContentFile(base64.b64decode(imgstr))
    event = Event.objects.get(id=event_id)
    event.image.delete(False)
    uid = uuid.uuid4()
    event.image.save('image_for_event_id_' + str(event_id) +
                     '_' + str(uid) + '.' + ext, data_image)

    data = {
        # 'values': values
        'values': 'ok'
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def convert_data_to_image_per_guest(request):
    json_values = simplejson.dumps(request.body)  # convert to json values
    string_values = json.loads(json_values)  # convert to string
    dictionary_values = ast.literal_eval(
        string_values)  # convert to dictionary
    format, imgstr = dictionary_values['data'].split(';base64,')
    guest_id = dictionary_values['guest_id']

    ext = format.split('/')[-1]
    data_image = ContentFile(base64.b64decode(imgstr))

    guest = Guest.objects.get(pk=guest_id)
    guest.image.save('image_for_guest_id_' +
                     str(guest_id) + '.' + ext, data_image)
    data = {
        # 'values': values
        'values': guest_id
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def get_image_state(request):
    event = Event.objects.get(id=request.GET.get('event_id', None))
    data = {'has_values': False, 'state': None}
    if event.image_state:
        file_path = 'media/' + str(event.image_state)
        data_file = open(file_path, 'r')
        data = {'has_values': True, 'state': data_file.read()}
    return JsonResponse(data, safe=False)


@csrf_exempt
def get_image_state_per_guest(request):
    guest = Guest.objects.get(id=request.GET.get('guest_id', None))
    file_path = 'media/' + str(guest.svg)
    doc = minidom.parse(file_path)  # parseString also exists
    for path in doc.getElementsByTagName('path'):
        guest_svg_d_path = path.getAttribute('d')

    event = Event.objects.get(id=request.GET.get('event_id', None))
    file_path = 'media/' + str(event.image_state)
    with open(file_path) as f:
        json_data = json.load(f)
    json_data['canvas']['objects'][1]['path'] = guest_svg_d_path
    data = {'has_values': True, 'state': json_data}

    with open('media\generic_qr_code.txt', 'r') as reader:
        print(reader.read())

    return JsonResponse(data, safe=False)

    event = Event.objects.get(id=request.GET.get('event_id', None))
    data = {'has_values': False, 'state': None}
    if event.image_state:
        file_path = 'media/' + str(event.image_state)
        data_file = open(file_path, 'r')
        data = {'has_values': True, 'state': data_file.read()}
    return JsonResponse(data, safe=False)


def update_svg_in_event_state(svg, json_data, static_qr_code):
    result = copy.deepcopy(json_data)  # to avoid pass by reference
    for i in result['canvas']['objects']:
        if (isinstance(i, dict)):
            for key in i:
                if (key == 'path' and str(i[key]) == static_qr_code):

                    i[key] = svg
    return result


@csrf_exempt
def getGuestIDs(request):

    event_id = request.GET.get('event_id', None)
    event = Event.objects.get(id=event_id)
    file_path = 'media/' + str(event.image_state)
    with open(file_path) as f:
        json_data = json.load(f)
    with open('media/static_qr_code.txt', 'r') as reader:
        static_qr_code = reader.read()

     # this for new added guests that does not have state
    if(event.is_state_update == False):
        guests = Guest.objects.filter(event_id=event_id, state='')
    else:
        guests = Guest.objects.filter(event_id=event_id)

    thislist = []
    for guest in guests:
        file_path = 'media/' + str(guest.svg)
        doc = minidom.parse(file_path)
        for path in doc.getElementsByTagName('path'):
            guest_svg_d_path = path.getAttribute('d')

        result = update_svg_in_event_state(
            guest_svg_d_path, json_data.copy(), static_qr_code)
        json_values = simplejson.dumps(result)
        guest.state.save('state_for_guest_id_' + str(guest.id) +
                         '.json', ContentFile(json_values))
        thisdict = {
            "event_id": event_id,
            "guest_id": guest.id,
            "guest_state": json_values
        }
        thislist.append(thisdict)

    return JsonResponse(thislist, safe=False)


@csrf_exempt
def save_image_state(request, event_id):
    event = Event.objects.get(id=event_id)
    json_data = json.loads(str(request.body, encoding='utf-8'))
    state = json_data['state']
    event.is_state_update = True
    event.image_state.save('state_for_event_id_' +
                           str(event_id) + '.json', ContentFile(state))

    data = {
        'message': 'ok'
    }
    return JsonResponse(data)


def export_guest(request, event_id):
    guest_resource = GuestResource()
    queryset = Guest.objects.filter(event_id=event_id)
    dataset = guest_resource.export(queryset)
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="guest.xls"'
    return response


def import_guest_save(request, event_id):
    if request.method == 'POST':
        excel_first_column = request.POST.get('select-headers')
        person_resource = GuestResource()
        dataset = Dataset()
        add_fk_to_imported_data = Dataset()

        new_guests = request.FILES['myfile']
        imported_data = dataset.load(new_guests.read())
        add_fk_to_imported_data.headers = ('event_id', 'guest_name')

        for c in imported_data[excel_first_column]:
            add_fk_to_imported_data.append((event_id, c))
    person_resource.import_data(
        add_fk_to_imported_data, dry_run=False)  # Actually import now
    return redirect(reverse('guests', args=(event_id,)))


@csrf_exempt
def import_guest_validate(request):
    if request.method == 'POST':
        form = FileUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            dataset = Dataset()
            guests_file = request.FILES['myfile']
            imported_data = dataset.load(guests_file.read())
        else:
            print('invalid form')
            print(form.errors)
    data = {
        'imported_data': imported_data.headers
    }
    return JsonResponse(list(imported_data.headers), safe=False)


def updateevent(request, dataset_id):
    if request.method == 'POST':
        json_values = simplejson.dumps(request.POST)
        try:
            d = json.loads(json_values)
            if d['name'].startswith('eventname'):
                t = Event.objects.get(id=dataset_id)
                t.event_name = d['value']
                t.save()
            if d['name'].startswith('eventdate'):
                t = Event.objects.get(id=dataset_id)
                t.event_date = d['value']
                t.save()
        except KeyError:
            HttpResponseServerError("Malformed data!")
        return HttpResponse(json_values, content_type='application/json')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'invitation/delete_event.html'
    success_message = 'Success: Event was deleted.'
    success_url = reverse_lazy('events')


class EventCreateView(CreateView):
    template_name = 'invitation/create_event.html'
    form_class = EventsForms
    success_message = 'Success: Event was created.'
    success_url = reverse_lazy('events')


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'invitation/update_event.html'
    form_class = EventsForms
    success_message = 'Success: Event was updated.'
    success_url = reverse_lazy('events')


class GuestCreateView(CreateView):
    model = Guest
    template_name = 'invitation/create_guest.html'
    form_class = GuestPopupForm
    success_message = 'Success: Guest was created.'

    def form_valid(self, form):
        form.save(commit=False)
        event_id = Event.objects.get(id=self.kwargs['event_id'])
        form.instance.event_id = event_id
        form.save()
        return redirect('guests', event_id=self.kwargs['event_id'])

        # form.save(commit=False)
        # event_id= Event.objects.get(id=self.kwargs['event_id'])
        # form.instance.event_id = event_id
        # form.save()
        # return redirect('guests', event_id=self.kwargs['event_id'])
    # def get_success_url(self):
    #     return reverse('guests',kwargs={'event_id': self.kwargs['event_id']})


class GuestCreateViewInEventPage(CreateView):
    template_name = 'invitation/create_guest.html'
    form_class = GuestPopupForm
    success_message = 'Success: Guest was created.'

    def form_valid(self, form):
        form.save(commit=False)
        event_id = Event.objects.get(id=self.kwargs['event_id'])
        form.instance.event_id = event_id
        form.save()
        return redirect('events')


class GuestDeleteView(DeleteView):
    model = Guest
    template_name = 'invitation/delete_guest.html'
    success_message = 'Success: Guest was deleted.'

    def get_success_url(self):
        return reverse('guests', kwargs={'event_id': self.kwargs['event_id']})


class GuestUpdateView(UpdateView):
    model = Guest
    template_name = 'invitation/update_guest.html'
    form_class = GuestPopupForm
    success_message = 'Success: Guest was updated.'

    def get_success_url(self):
        return reverse('guests', kwargs={'event_id': self.kwargs['event_id']})


@login_required
def events(request):
    events = Event.objects.filter(user_id=request.user).annotate(
        guest_count=Count('guest__event_id'))
    return render(request, 'invitation/events.html', {'events': events, 'events_nav': 'active'})


class EventReadView(BSModalReadView):
    model = Event
    template_name = 'invitation/read_event.html'


def dashboard(request, event_id):
    events = Event.objects.all
    gustes = Guest.objects.filter(event_id=event_id)
    total_gustes = Guest.objects.filter(event_id=event_id).count()
    total_present = Guest.objects.filter(
        check_in_date__isnull=False, event_id=event_id).count()
    total_not_show = Guest.objects.filter(
        check_in_date__isnull=True, event_id=event_id).count()
    attendance_ratio = 0
    if (total_gustes):
        attendance_ratio = round((total_present / total_gustes) * 100, 1)
    return render(request, 'invitation/dashboard.html',
                  {'events': events, 'gustes': gustes, 'total_gustes': total_gustes, 'total_present': total_present,
                   'total_not_show': total_not_show, 'attendance_ratio': attendance_ratio, 'selected_event': event_id})


def handler404(request):
    return render(request, 'invitation/editor.html', status=404)


@login_required
def guests(request, event_id=None):

    if event_id:
        events = Event.objects.filter(user_id=request.user)
        # post = get_object_or_404(Event, pk=event_id)
        guests = Guest.objects.filter(event_id=event_id)
        event_name = Event.objects.get(
            id=event_id, user_id=request.user).event_name
        context = {'events': events, 'event_name': event_name, 'guests': guests, 'event_id': event_id, 'guests_nav': 'active',
                   'invoice_header_section': 'display:flex',
                   'display_flex': 'display:none', 'display': 'display:none', 'display_block': 'display:block', }

        return render(request, 'invitation/guests.html', context)
    # xx=Guest.objects.all()[:1]
    events = Event.objects.filter(user_id=request.user)
    return render(request, 'invitation/guests.html',
                  {'events': events, 'guests_nav': 'active', 'display_flex': 'display:flex',
                   'invoice_header_section': 'display:none',
                   'display_none': 'display:none', 'display': 'display:block'})


@csrf_exempt
def guest_list_json(request):
    event_id = request.GET.get('event_id', None)
    print(event_id)
    # wrap in list(), because QuerySet is not JSON serializable
    data = list(Guest.objects.filter(event_id=event_id).values())
    return JsonResponse({'data': data})


def download_images(request, event_id):
    file_directory = 'media/event_id_' + str(event_id) + '/image/'
    zip_file_name = 'event_id_' + str(event_id) + '.rar'
    zip = ZipFile(zip_file_name, 'w')
    for single_file in os.listdir(file_directory):
        zip.write(file_directory + single_file, single_file)
    zip.close()

    wrapper = FileWrapper(open(zip_file_name, 'rb'))
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=' + zip_file_name
    event = Event.objects.get(pk=event_id)
    event.is_state_update = False
    event.save()
    return response


def download(request, event_id):
    event_image = Event.objects.get(id=event_id)
    event_image_url = event_image.image
    file_directory = 'media/' + str(event_image_url)
    wrapper = FileWrapper(open(file_directory, 'rb'))
    content_type = mimetypes.guess_type(file_directory)[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename=' + \
        'image_for_event_id_' + str(event_id) + '.png'
    return response
