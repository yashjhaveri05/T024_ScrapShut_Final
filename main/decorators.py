from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *

def ngo_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.is_NGO:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func 

def donor_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        if user.is_Donor:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func 
