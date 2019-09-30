from django.contrib import admin
from app1.models import UserRole
from app1.models import MySiteUser
from app1.models import UserImage


# Register your models here.
admin.site.register(UserRole)
admin.site.register(MySiteUser)
admin.site.register(UserImage)
