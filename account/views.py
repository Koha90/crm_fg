from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import LoginForm


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