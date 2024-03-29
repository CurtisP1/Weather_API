#  Copyright (c) 2023 - All rights reserved.
#  Created by Curtis Poon for PROCTECH 4IT3/SEP 6IT3.
#  SoA Notice: I Curtis Poon, 400263978 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

# from django.contrib.auth import authenticate, login as auth_login
# from accounts.forms import UserLoginForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect
# from django.contrib.auth.hashers import *
#
#
# @login_required(login_url='/accounts/login/')
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST or None)
#         if form.is_valid():
#             username = User.objects.get(email=form.cleaned_data['email'])
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user:
#                 if user.is_active:
#                     auth_login(request, user)
#                     return HttpResponseRedirect(request.GET.get('next', settings.LOGIN_REDIRECT_URL))
#             else:
#                 error = 'Invalid username or password.'
