from django.contrib import admin
from django.db import models

from .models import Pet, Vaccine

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']

# @admin.register(Vaccine)
# class VaccineAdmin



