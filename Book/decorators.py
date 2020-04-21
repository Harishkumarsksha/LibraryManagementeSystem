from django.shortcuts import redirect
from django.http import HttpResponse


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'Student':
                return redirect('/')

            if group == 'Admin':
                return view_func(request, *args, **kwargs)

    return wrapper_function