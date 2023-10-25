from django.contrib import admin
from .models import url_model, login_model

admin.site.register(url_model)
admin.site.register(login_model)
