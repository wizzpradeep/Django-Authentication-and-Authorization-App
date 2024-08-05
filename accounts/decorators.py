from django.shortcuts import redirect
from django.contrib import messages

def login_required(func):
    def wrapper(request, *args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You must login")
            return redirect('login')
        return func(request,*args,**kwargs)
    return wrapper  


def user_is_authenticated(func):
    def wrapper(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return func(request,*args,**kwargs)
    return wrapper  
