from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.decorators import login_required

from .models import Client
from .forms import ClientForm


@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'crm/client/list.html', {'clients': clients})


@login_required
def client_detail(request, client, id):
    client = get_object_or_404(Client, id=id, slug=client)
    return render(request, 'crm/client/detail.html', {'client': client})


@login_required
def client_new(request):
    form = ClientForm()
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.responsible = request.user
            client.save()
            return redirect('crm:client_list')
    else:
        client_form = ClientForm()
    return render(request, 'crm/client/edit.html', {'client_form': client_form})


@login_required
def client_edit(request, id, client):
    client = get_object_or_404(Client, id=id, slug=client)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.save()
            # Это сделано. Внимательно изучить ещё раз
            return redirect('crm:client_detail', id=client.id, client=client.slug)
    else:
        client_form = ClientForm(instance=client)
    return render(request, 'crm/client/edit.html', {'client_form': client_form})
