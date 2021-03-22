from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote, Person
import random

# Create your views here.

class HomePageView(ListView):
    """
        Show a listing of Quotes.
    """
    model = Quote #restieve Quote objects from teh database
    template_name = "quotes/home.html"
    context_object_name = "quotes"

class QuotePageView(DetailView):
    """
        Display single quote object.
    """
    model = Quote #restieve Quote objects from teh database
    template_name = "quotes/quote.html" #delagate the display to this template
    context_object_name = "quote" # use this variable name in the template

class RandomQuotePageView(DetailView):
    """
        Display single quote object, chosen at random.
    """
    model = Quote #restieve Quote objects from teh database
    template_name = "quotes/quote.html"
    context_object_name = "quote"
    
    def get_object(self):
        """
            Select one quote at random form display in teh quote.html template
        """

        #obtain all quotes using the object manager
        quotes = Quote.objects.all()
        #select one at random
        q = random.choice(quotes)
        return q

class PersonPageView(DetailView):
    """
        Display quotes of one person.
    """
    model = Person #restieve Quote objects from teh database
    template_name = "quotes/person.html" #delagate the display to this template
    context_object_name = "person" # use this variable name in the template
