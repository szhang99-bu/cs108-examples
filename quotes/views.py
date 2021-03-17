from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote

# Create your views here.

class HomePageView(ListView):
    """
        Show a listing of Quotes.
    """
    model = Quote #restieve Quote objects from teh database
    template_name = "quotes/home.html"
    context_object_name = "quotes"
