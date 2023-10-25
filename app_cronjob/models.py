from django.db import models

class login_model(models.Model):
    id=models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100,default="")
    user_email = models.EmailField(max_length=100,default="")
    user_password = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.user_name

class url_model(models.Model):
    id=models.AutoField(primary_key=True)
    user_email = models.EmailField(max_length=100,default="")
    url_link  = models.CharField(max_length=280,default="")
    status_code = models.CharField(max_length=20,default="")
    status_message  = models.CharField(max_length=80,default="")
    date_checked  = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
