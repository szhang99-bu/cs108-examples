from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Quote, Person
import random
from .forms import CreateQuoteForm, UpdateQuoteForm, AddImageForm


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
    # context_object_name = "person" # use this variable name in the template

    def get_context_data(self, **kwargs):
        """
            Return a dictionary with data for this template to use
        """
        # get the defuld context data
        # this will include the person record for this page view
        context = super(PersonPageView, self).get_context_data(**kwargs)

        #create the add inmage form:
        add_image_form = AddImageForm()
        context['add_image_form'] = add_image_form

        #return context dictionary
        return context

class CreateQuoteView(CreateView):
    """
        Create a new quote object and store it in the database
    """

    model = Quote # which model to create
    form_class = CreateQuoteForm
    template_name = "quotes/create_quote_form.html"

class UpdateQuoteView(UpdateView):
    """
        Create a new quote object and store it in the database
    """

    model = Quote # which model to create
    form_class = UpdateQuoteForm
    template_name = "quotes/update_quote_form.html"

class DeleteQuoteView(DeleteView):
    """
        Create a new quote object and store it in the database
    """

    model = Quote
    template_name = "quotes/delete_quote.html"
    # success_url = "../../all" #what to do after delete

    def get_success_url(self):
        """
            Return the URL to which we should be directed after the delete
        """

        # get the pk for this quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first() #get one object from 

        # find the person associated with the quote
        person = quote.person
        return reverse('person', kwargs = {'pk':person.pk})
    
def add_image(request, pk):
    """
        A custom view function to handle the submission of an image uploaded
    """
    
    #find the person object for whom we are submistting the image
    person = Person.objects.get(pk=pk)
    
    # read request data into AddImageForm object
    form = AddImageForm(request.POST or None, request.FILES or None)
    
    # Check is the form is valid
    if form.is_valid():
        image = form.save(commit=False) #create the image object
        image.person = person
        image.save()

    else:
        print("Error: the form was not valid")
    
    # redirect to a new URL, display poerson page
    url = reverse('person', kwargs = {'pk':pk})
    return redirect(url)