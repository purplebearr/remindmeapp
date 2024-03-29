from django.contrib import admin

# Register your models here.

from .models import User, Reminder
admin.site.register(User)
admin.site.register(Reminder)
