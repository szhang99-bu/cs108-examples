from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile
from .forms import CreateProfileForm, UpdateProfileForm


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

class CreateProfileView(CreateView):
    """
        Create a new profile object and store it in the database
    """

    model = Profile # which model to create
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

class UpdateProfileView(UpdateView):
    """
        Create a new quote object and store it in the database
    """

    model = Profile # which model to create
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"