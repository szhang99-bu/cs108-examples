from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.urls import reverse


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
    
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view

        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        # create a new CreateStatusMessageForm, and add it into the context dictionary

        form = CreateStatusMessageForm() 
        context['create_status_form'] = form

        # return this context dictionary
        return context

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

class DeleteStatusMessageView(DeleteView):
    """
        TO delete a posted static message
    """
    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        """
        Return the context data to be used in the template
        """
        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        # Find the status message object that we are trying to delete, and save it to a variable.
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg
        # return this context dictionary
        return context

    def get_object(self):
        """
        access the parameters dictionary to read these URL data values, and find out which to delete
        """

        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        message_object = StatusMessage.objects.filter(pk=status_pk)

        return message_object
        
    def get_success_url(self):
        """
        Return a the URL to which we should be directed after the delete
        """

        # get the pk for this quote
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # # reverse to show the person page.
        return reverse('show_profile_page', kwargs={'pk':profile_pk})
    


def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet
            image = form.save(commit=False)

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile
            image.profile = profile

            # now commit to database
            #create the image object   
            image.save()
            status_message.save()
            
        else:
            print("Error: the form was not valid")

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)