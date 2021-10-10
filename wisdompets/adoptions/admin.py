from django.contrib import admin


# This file is used to allow admin to see and edit the data
# To create a super user use the following command:
#   python3 manage.py createsuperuser

#importing pet model from the models.py
from .models import Pet

#Register class with admin to say what's it associated with 
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    # States the categories that yu want to be displayed in the admin panel
    list_display = ['name', 'breed', 'age', 'sex']
