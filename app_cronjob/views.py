from django.shortcuts import render, redirect
from . import forms; from .models import *
import requests


# Create your views here.


def auth(method):
    def wrapper(request):
        if request.session.get('currentUser', False):
            return method(request)
        else:
            return redirect("login")
    return wrapper

def status_message(status_code):
    stats=str(status_code)
    if stats == "200":
        return "Site is working fine"
    elif stats == "400":
        return "Bad request"
    elif stats == "403":
        return "Forbidden request"
    elif stats == "404":
        return "Page does not exist"
    elif stats == "405":
        return "method not allowed"
    elif stats == "500":
        return "Internal server error"
    elif stats == "503":
        return "service Unavailable"
    else:
        return "Unidentified"

def register(request):
    if request.method == "POST":
        new_user = forms.registeration_form(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect("login")
        else:
            return render(request, 'register.html', {"form": new_user})
    else:
        _new_user = forms.registeration_form(None)
        return render(request, 'register.html', {"form": _new_user})

def login(request):
    if request.method == "POST":
        user_login = forms.login_form(request.POST)
        if user_login.is_valid():
            request.session["currentUser"] = user_login.cleaned_data["user_email"]
            return redirect("profile")
        else:
            return render(request, 'login.html', {"form": user_login})
    else:
        _user_login = forms.login_form(None); request.session["currentUser"]=False
        return render(request, 'login.html', {"form": _user_login})

@auth
def profile(request):
    current_user = request.session.get('currentUser')
    user_name = login_model.objects.values_list("user_name", flat=True).get(user_email=current_user)
    url_record = url_model.objects.filter(user_email=current_user).values()
    if request.method == "POST":
        form_data = request.POST.copy()
        form_data.update({'user_email': current_user})
        check_url = forms.url_form(form_data)
        if check_url.is_valid():
            url = check_url.cleaned_data["url_link"]
            try:
                response = requests.get(url);status_code=response.status_code;_status_message=status_message(status_code)
                check_url.save()
                current_url_id_query =  url_model.objects.filter(user_email=current_user).order_by('-id')
                current_url_id=current_url_id_query.values()[0]["id"]
                url_model.objects.filter(id=current_url_id).update(user_email=current_user, status_code=status_code, status_message=_status_message)
                context = {"url":url, "status_code":status_code, "status_message":_status_message}
                return render(request, "results.html", context)
            except Exception as e:
                print(e);return render(request, 'profile.html', {"form": check_url, "user_name": user_name.title(), "url_record":url_record, "msg":"Unable to check link"})
        else:
            return render(request, 'profile.html', {"form": check_url, "user_name": user_name.title(), "url_record":url_record})
    else:
        _check_url = forms.url_form(None)
        return render(request, 'profile.html', {"form": _check_url, "user_name": user_name.title(), "url_record":url_record})


