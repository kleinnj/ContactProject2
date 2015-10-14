from django.shortcuts import render
from django.views import generic
from .models import Contact


class IndexView(generic.ListView):
    
    template_name = "contact/index.html"
    context_object_name = "contact_list"
    
    def get_queryset(self):
        return Contact.objects.order_by('contact_first_name')
    