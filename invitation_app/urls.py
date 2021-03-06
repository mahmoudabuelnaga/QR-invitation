from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('design/<int:event_id>', views.design, name='design'),
    #     path('accounts/signup/', views.signup, name='signup'),
    #    path('accounts/login/', views.user_login, name='user_login'),
    #    path('user_logout/', views.user_logout, name='user_logout'),
    path('import_guest_validate/', views.import_guest_validate,
         name='import_guest_validate'),
    path('import_guest_save/<int:event_id>',
         views.import_guest_save, name='import_guest_save'),
    path('basic_calendar', TemplateView.as_view(
        template_name="basic-calendar.html"), name='basic_calendar'),
    path('guests', views.guests, name='guests'),
    path('guest_list_json', views.guest_list_json, name='guest_list_json'),
    path('guests/<int:event_id>', views.guests, name='guests'),
    path('create_event/', views.EventCreateView.as_view(), name='create_event'),
    path('update/<int:pk>', views.guests, name='update_event'),
    path('read_event/<int:pk>', views.EventReadView.as_view(), name='read_event'),
    path('create_guest/<int:event_id>',
         views.GuestCreateView.as_view(), name='create_guest'),
    path('create_guest_in_event_page/<int:event_id>',
         views.GuestCreateViewInEventPage.as_view(), name='create_guest_in_event_page'),
    path('update_guest/<int:pk>/<int:event_id>',
         views.GuestUpdateView.as_view(), name='update_guest'),
    path('delete_guest/<int:pk>/<int:event_id>',
         views.GuestDeleteView.as_view(), name='delete_guest'),
    path('export_guest/<int:event_id>', views.export_guest, name='export_guest'),
    path('delete/<int:pk>', views.guests, name='delete_event'),
    path('delete_event/<int:pk>',
         views.EventDeleteView.as_view(), name='delete_event'),
    path('update_event/<int:pk>',
         views.EventUpdateView.as_view(), name='update_event'),
    path('updateevent/<int:dataset_id>', views.updateevent, name='updateevent'),
    path('events', views.events, name='events'),
    path('editor', TemplateView.as_view(
        template_name="editor.html"), name='editor'),
    path('mynotes', TemplateView.as_view(
        template_name="mynotes.html"), name='mynotes'),
    path('download_images/<int:event_id>',
         views.download_images, name='download_images'),
    path('download/<int:event_id>', views.download, name='download'),
    path('save_image_state/<int:event_id>',
         views.save_image_state, name='save_image_state'),
    path('get_image_state/', views.get_image_state, name='get_image_state'),
    path('convert_data_to_image/<int:event_id>',
         views.convert_data_to_image, name='convert_data_to_image'),
    path('convert_data_to_image_per_guest/', views.convert_data_to_image_per_guest,
         name='convert_data_to_image_per_guest'),
    path('getGuestIDs/', views.getGuestIDs, name='getGuestIDs'),
    # path('get_image_state_per_guest/', views.get_image_state_per_guest, name='get_image_state_per_guest'),

]
