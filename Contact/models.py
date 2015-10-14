from django.db import models
from User.models import User



# Create your models here.
#This file contains the Contact object models

class Contact(models.Model):

    contact_first_name = models.CharField(max_length= 50)
    contact_last_name = models.CharField(max_length = 50)
    contact_phone_number = models.CharField(max_length = 10)
    contact_email_address = models.EmailField(max_length = 50)
    contact_street_address = models.CharField(max_length = 100)

    
    
    def __str__(self):
        return self.contact_first_name + self.contact_last_name
    
    
    