from django.contrib import admin

# Register your models here.
from .models import Profiles, City


admin.site.register(Profiles)
admin.site.register(City)