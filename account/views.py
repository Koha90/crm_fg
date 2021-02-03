from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)  # Создаём объект формы с данными.
#         if form.is_valid():  # Проверяем, правильно ли она заполненна.
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Авторизация прошла успешно!')
#                 else:
#                     return HttpResponse('Аккаунт заблокирован')
#             else:
#                 return HttpResponse('Неверный логин')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})