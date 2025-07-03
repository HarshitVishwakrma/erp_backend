# models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

from django.conf import settings

class MyModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)  # store as plain text (⚠️ insecure)
    PlantName = models.CharField(max_length=90)
    Department = models.CharField(max_length=100)
    FullName = models.CharField(max_length=100)
    MobileNo = models.CharField(max_length=100)

    def __str__(self):
        return self.FullName



class Module(models.Model):
    name = models.CharField(max_length=100)

class UserPermission(models.Model):
    user = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)


# Creating FinancialYear
class FinancialYear(models.Model):
    FyName = models.CharField(max_length=100)
    From_Date = models.DateField()
    To_Date = models.DateField()
    ShortName = models.CharField(max_length=10, unique=True)  # Enforcing uniqueness on ShortName

    def __str__(self):
        return self.FyName

