from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm, ProfileForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
# Create your views here.


# class Signup(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


@login_required
def profile(request):
    return render(request, 'registration/profile.html', {})


# class profile_seetings(UpdateView, LoginRequiredMixin):
#     model = Profile
#     form_class = ProfileUpdateForm
#     success_url = reverse_lazy('profile')
#     template_name = 'registration/user_account_setting.html'


@login_required
def profile_settings(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(instance=request.user, data=request.POST)
        p_form = ProfileUpdateForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'registration/user_account_setting.html', context)


@transaction.atomic
def create_user_view(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():  # and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            # Reload the profile form with the profile instance
            profile_form = ProfileForm(request.POST, instance=user.profile)
            # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.full_clean()
            profile_form.save()  # Gracefully save the form
        return redirect('login')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registration/signup.html', context)
