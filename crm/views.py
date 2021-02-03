from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import ClientEditForm


@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client/list.html', {'clients': clients})

@login_required
def client_detail(request, client, id):
    client = get_object_or_404(Client, id=id, slug=client)
    return render(request, 'crm/client/detail.html', {'client': client})
