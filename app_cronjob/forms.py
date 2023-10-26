from django import forms
from .models import login_model, url_model

class registeration_form(forms.ModelForm):
    class Meta:
        model = login_model
        fields = ("user_name","user_email", "user_password")
        labels = {"user_name":"Full Name", "user_email":"Email","user_password":"Password"}

    def clean_user_email(self, *args, **kwargs):
        _user_email = self.cleaned_data.get("user_email"); _user_email=_user_email.lower()
        checker = login_model.objects.filter(user_email=_user_email).exists()
        if checker:
            raise forms.ValidationError("Email already exists, please use anothe one")
        else:
            return _user_email

class login_form(forms.ModelForm):
    class Meta:
        model = login_model
        fields = ("user_email", "user_password")
        labels = {"user_email":"Email","user_password":"Password"}
        help_texts = {"user_password":"Your password is case sensitive"}

    def clean_user_email(self, *args, **kwargs):
        _user_email = self.cleaned_data.get("user_email"); _user_email=_user_email.lower()
        checker = login_model.objects.filter(user_email=_user_email)
        if checker:
            return _user_email
        else:
            raise forms.ValidationError("Incorrect email")

class url_form(forms.ModelForm):
    class Meta:
        model = url_model
        fields = ("url_link","user_email")
        labels = {"url_link": "Enter URL"}
        help_texts = {"url_link":"Enter the url you wish to check, start with https://"}
        widgets = {"user_email": forms.HiddenInput()}


    def clean_url_link(self, *args, **kwargs):
        _url_link = self.cleaned_data.get("url_link")
        _url_link = _url_link.lower(); protocols = ["http", "https"]
        check_protocol = _url_link.split(":"); check_slashes = _url_link.split("//")
        error_message = "Ensure you start the url link with https:// or http://"
        if check_protocol[0] not in protocols:
            raise forms.ValidationError(error_message)
        elif len(check_slashes) < 2:
            raise forms.ValidationError(error_message)
        else:
            return _url_link



