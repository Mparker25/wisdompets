# Base class for all models
from django.db import models

# These are the models needed to create instances for the pets. 
#   We'll store these instances into databases with the classes 
#   defining the model and the attributes related to each object.

# After this we have to create migrations incase we update these models
# Why?: They may already exist in the database and if we update the model
#       We can migrate the new info to the existing info on the database
#       Updates include:
#           Adding a Model
#           Adding a Field
#           Removing a Field
#           Changing a Field

# Initial Migrations
#   Creating tables for the models that are defined in models.py
#   Commands for Migrations
#       python3 manage.py makemigrations
#           - Generate migration files
#       python3 manage.py showmigrations
#       python3 manage.py migrate

# Unapplied Migration
#   When a migration file has been created, but hasn't been run
#   **Common error with new developers**

# Making a pet model
class Pet(models.Model):
    # This is how you define the choices in a list field
    # Each item in the list is stored as: 
    #   (Storage Value, Display Value)
    SEX_CHOICES = [('M', 'Male'), ('F','Female')]

    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)

    # Not all pets have breeds so it's ok to leave blank
    # (AKA: this isn't required)
    breed = models.CharField(max_length=30, blank=True)

    # Text Fields are used for unrestricted length fields
    description = models.TextField()

    # Choices Attribute
    # Not all pets will have a sex (hence blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)

    submission_date = models.DateTimeField()

    # For integers a blank value will translate to a 0
    # The age may be unknown so we'll use NULL instead
    age = models.IntegerField(null=True)

    # Requires a first argument with the name of the model it's related to as a string
    # Some pets may not have any vaccincaitons so (Blank= true)
    vaccinations = models.ManyToManyField('Vaccine',blank=True)

    # Tells what the string rep should be for this object
    def __str__(self):
        # use the name field as the default representation for the vaccine
        return self.name

# Making a Vaccine Model
class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    # Tells what the string rep should be for this object
    def __str__(self):
        # use the name field as the default representation for the vaccine
        return self.name
