from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    """
        Show a listing of Quotes.
    """
    model = Profile #restieve Quote objects from teh database
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    """
        Display single quote object.
    """
    model = Profile #restieve Profile objects from the database
    template_name = "mini_fb/show_profile_page.html" #delagate the display to this template
    context_object_name = "profiles" # use this variable name in the template