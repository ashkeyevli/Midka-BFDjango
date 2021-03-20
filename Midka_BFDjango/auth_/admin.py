from django.contrib import admin

# Register your models here.
from auth_.models import MainUser, UserProfile

admin.site.register(MainUser)
admin.site.register(UserProfile)