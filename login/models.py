from django.db import models

class Accounts(models.Model):
    logins = models.CharField("Логин", max_length=50)
    password = models.CharField("Пароль", max_length=200)

    def __str__(self):
        return self.logins

# Create your models here.
