from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    """
        a form to create a new quote object
    """
    first_name = forms.CharField(label="First Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email", required=True)

    class Meta:
        """
            Additional data about this form
        """
        model = Profile #which model to create
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email', 'image_url']


class UpdateProfileForm(forms.ModelForm):
    """
        a form to update a new quote object
    """
    first_name = forms.CharField(label="First Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email", required=True)
    class Meta:
        """
            Additional data about this form
        """
        model = Profile #which model to create
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email', 'image_url']
