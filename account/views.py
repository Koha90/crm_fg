from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserEditForm, ProfileEditForm


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'account/profile/list.html', {'profiles': profiles})


@login_required
def profile_detail(request, profile, id):
    profile = get_object_or_404(Profile, id=id, slug=profile)
    return render(request, 'account/profile/detail.html', {'profile': profile})


@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('account:profile_detail', id=request.user.id, profile=request.user.profile.slug)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/profile/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})
