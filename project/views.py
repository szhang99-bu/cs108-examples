from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ShowAllComputerParts(ListView):
    """
        Show a listing of all the Computer Parts
    """
    model = ComputerParts # Using the Computer Part model for this page
    template_name = "project/show_all_computer_parts.html" #indicating which html is this view for 
    context_object_name = "parts"#give a contact name

class ShowSuccessView(ListView):
    """
        Show the purchase was successful
    """
    model = ComputerParts # Using the Computer Part model for this page
    template_name = "project/congratulation.html" #indicating which html is this view for 
    context_object_name = "parts"#give a contact name

class ShowProductPageView(DetailView):
    """
        Display single computer part object.
    """
    model = ComputerParts # Using the Computer Part model for this page
    template_name = "project/show_computer_part_page.html"#indicating which html is this view for 
    context_object_name = "parts"
    
# class CreateProfileView(CreateView):
#     """
#         Create a new user profile object and store it in the database
#     """

#     model = User # which model to create
#     form_class = CreateUserForm
#     template_name = "project/create_user_profile_page.html"

# class CreateAnAskView(LoginRequiredMixin, CreateView):
#     """
#         Create a new user profile object and store it in the database
#     """

#     model = Ask # which model to create
#     form_class = CreateAskForm
#     template_name = "project/make_an_ask_page.html"
#     login_url = "/login/"

class ShowMakeBidView(LoginRequiredMixin, DetailView):
    """
        Show the make a new bid page
    """
    model = ComputerParts # Using the Computer Part model for this page
    template_name = "project/make_a_bid_page.html"#indicating which html is this view for 
    context_object_name = "parts" #give a contact name
    login_url = "/login/" #redirect the user to the login page if they are not loged in

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view

        context = super(ShowMakeBidView, self).get_context_data(**kwargs)

        # create a new CreateStatusMessageForm, and add it into the context dictionary

        form = CreateBidForm() 
        context['create_bid_form'] = form

        # return this context dictionary
        return context

class ShowMakeAskView(LoginRequiredMixin, DetailView):
    """
        Show the purchase was successful
    """
    model = ComputerParts # Using the Computer Part model for this page
    template_name = "project/make_an_ask_page.html" #indicating which html is this view for 
    context_object_name = "parts"#give a contact name
    login_url = "/login/" #redirect the user to the login page if they are not loged in

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view

        context = super(ShowMakeAskView, self).get_context_data(**kwargs)

        # create a new CreateStatusMessageForm, and add it into the context dictionary

        form = CreateAskForm() 
        context['create_ask_form'] = form

        # return this context dictionary
        return context

def create_ask(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateAskForm(request.POST or None)
        
        if form.is_valid():

            # create the ask object with the data in the CreateStatusMessageForm
            ask = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            part = ComputerParts.objects.get(pk=pk)

            # attach FK profile to this status message
            ask.product = part

            # now commit to database  
            ask.save()
            
        else:
            print("Error: the form was not valid")

    # redirect the user to the show_computer_part_page view
    url = reverse('show_computer_part_page', kwargs={'pk': pk})
    return redirect(url)


def create_bid(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateBidForm(request.POST or None)

        if form.is_valid():

            # create the ask object with the data in the CreateStatusMessageForm
            bid = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            part = ComputerParts.objects.get(pk=pk)

            # attach FK profile to this status message
            bid.product = part

            # now commit to database  
            bid.save()
            
        else:
            print("Error: the form was not valid")

    # redirect the user to the show_computer_part_page view
    url = reverse('show_computer_part_page', kwargs={'pk': pk})
    return redirect(url)
    
# class CreateABidView(LoginRequiredMixin, CreateView):
#     """
#         Create a new user profile object and store it in the database
#     """

#     model = Bid # which model to create
#     form_class = CreateBidForm
#     template_name = "project/make_a_bid_page.html"
#     login_url = "/login/"

class UpdateBidView(LoginRequiredMixin, UpdateView):
    """
        Create a new quote object and store it in the database
    """

    model = Bid # which model to create
    form_class = UpdateBidForm
    template_name = "project/update_a_bid.html"
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        """
        Return the context data to be used in the template
        """
        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(UpdateBidView, self).get_context_data(**kwargs)
        # Find the status message object that we are trying to delete, and save it to a variable.
        bid_info = Bid.objects.get(pk=self.kwargs['bid_pk'])
        context['bid_info'] = bid_info
        # return this context dictionary
        return context
    
    def get_object(self):
        """
        access the parameters dictionary to read these URL data values, and find out which to delete
        """

        # read the URL data values into variables
        product_pk = self.kwargs['product_pk']
        bid_pk = self.kwargs['bid_pk']

        # find the Bid object, and return it
        bid_object = Bid.objects.get(pk=bid_pk)

        return bid_object
    
    def get_success_url(self):
        """
        Return a the URL to which we should be directed after the update
        """

        # # reverse to show the person page.
        return "/project/success/"

class UpdateAskView(LoginRequiredMixin, UpdateView):
    """
        Create a new quote object and store it in the database
    """

    model = Ask # which model to create
    form_class = UpdateAskForm
    template_name = "project/update_an_ask.html"
    login_url = "/login/"

    def get_context_data(self, **kwargs):
        """
        Return the context data to be used in the template
        """
        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(UpdateAskView, self).get_context_data(**kwargs)
        # Find the status message object that we are trying to delete, and save it to a variable.
        ask_info = Ask.objects.get(pk=self.kwargs['ask_pk'])
        context['ask_info'] = ask_info
        # return this context dictionary
        return context

    def get_object(self):
        """
        access the parameters dictionary to read these URL data values, and find out which to delete
        """

        # read the URL data values into variables
        product_pk = self.kwargs['product_pk']
        ask_pk = self.kwargs['ask_pk']

        # find the Bid object, and return it
        ask_object = Ask.objects.get(pk=ask_pk)

        return ask_object
    
    def get_success_url(self):
        """
        Return a the URL to which we should be directed after the update
        """

        # # reverse to show the person page.
        return "/project/success/"