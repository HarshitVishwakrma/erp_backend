from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyModel,Module,UserPermission

# Register your models here
admin.site.register(MyModel)
admin.site.register(Module)
admin.site.register(UserPermission)
