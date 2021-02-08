from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.decorators import login_required

from .models import Client, Comment, Category
from .forms import ClientForm, CommentForm


@login_required
def client_list(request, category_slug=None):
    clients = Client.objects.all()
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        clients = clients.filter(category=category)
    return render(request, 'crm/client/list.html', {'clients': clients,
                                                    'categories': categories,
                                                    'category': category})


@login_required
def client_detail(request, client, id):
    client = get_object_or_404(Client, id=id, slug=client)
    comments = client.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # Комментарий отправлен.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Привязываем комментарий к клиенту
            new_comment.client = client
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'crm/client/detail.html', {'client': client,
                                                      'comments': comments,
                                                      'new_comment': new_comment,
                                                      'comment_form': comment_form})


@login_required
def client_new(request):
    client_form = ClientForm()
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.responsible = request.user
            client.save()
            return redirect('crm:client_list')
    else:
        client_form = ClientForm()
    return render(request, 'crm/client/edit.html', {'client_form': client_form, 'section': 'client_new'})


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
