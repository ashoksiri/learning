from django.http import HttpResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def welcome(request):
    return render(request=request,template_name='registration/login.html')