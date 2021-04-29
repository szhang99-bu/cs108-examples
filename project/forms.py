from django import forms
from .models import *

# class CreateUserForm(forms.ModelForm):
#     """
#         a form to create a new quote object
#     """
#     first_name = forms.CharField(label="First Name", required=True)
#     last_name = forms.CharField(label="Last Name", required=True)
#     address = forms.CharField(label="Mailing Address", required=True)
#     email = forms.CharField(label="Email", required=True)
#     phone_number = forms.CharField(label="Phone Number", required=True)

#     class Meta:
#         """
#             Additional data about this form
#         """
#         model = User #which model to create
#         fields = ['first_name', 'last_name', 'address', 'email', 'phone_number']

# class UpdateUserForm(forms.ModelForm):
#     """
#         a form to update a new quote object
#     """
#     first_name = forms.CharField(label="First Name", required=True)
#     last_name = forms.CharField(label="Last Name", required=True)
#     address = forms.CharField(label="Mailing Address", required=True)
#     email = forms.CharField(label="Email", required=True)
#     phone_number = forms.CharField(label="Phone Number", required=True)

#     class Meta:
#         """
#             Additional data about this form
#         """
#         model = User #which model to create
#         fields = ['first_name', 'last_name', 'address', 'email', 'phone_number']

class CreateAskForm(forms.ModelForm):
    """
        a form to create a new ask object
    """
    price = forms.DecimalField(label="Asking Price", required=True)
    email = forms.CharField(label="Email", required=True)
    phone_number = forms.CharField(label="Phone Number", required=True)

    class Meta:
        """
            Additional data about this form
        """
        model = Ask #which model to create
        fields = ['price', 'email', 'phone_number']

class CreateBidForm(forms.ModelForm):
    """
        a form to create a new bid object
    """
    price = forms.DecimalField(label="Biding Price", required=True)
    email = forms.CharField(label="Contact Email", required=True)
    phone_number = forms.CharField(label="Contact Phone Number", required=True)
    class Meta:
        """
            Additional data about this form
        """
        model = Bid #which model to create
        fields = ['price', 'email', 'phone_number']

class UpdateAskForm(forms.ModelForm):
    """
        a form to update a new quote object
    """
    sold = models.BooleanField(default=False)
    class Meta:
        """
            Additional data about this form
        """
        model = Ask #which model to create
        fields = ['sold']
    
    def __init__(self, *args, **kwargs):
        """
            an init feild overwite the original name sold to - confirm transaction
        """
        super(UpdateAskForm, self).__init__(*args, **kwargs)
        self.fields['sold'].label = "Confirm Transaction"

class UpdateBidForm(forms.ModelForm):
    """
        a form to update a new quote object
    """
    sold = models.BooleanField(default=False)
    class Meta:
        """
            Additional data about this form
        """
        model = Bid #which model to create
        fields = ['sold']

    def __init__(self, *args, **kwargs):
        """
            an init feild overwite the original name sold to - confirm transaction
        """
        super(UpdateBidForm, self).__init__(*args, **kwargs)
        self.fields['sold'].label = "Confirm Transaction"