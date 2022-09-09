from django.shortcuts import redirect
from django.http import HttpResponse

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):

            # print('working',allowed_roles)
            # print(request.user.groups.exists()) #True
            # print(request.user.groups.all())

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                # print(group)
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return redirect('accounts:user_page')
        return wrapper_func
    return decorator
