# forms.py

from django import forms
from .models import Quote

class CreateQuoteForm(forms.ModelForm):
    """
        a form to create a new quote object
    """
    class Meta:
        """
            Additional data about this form
        """
        model = Quote #which model to create
        fields = ['text', 'person']


class UpdateQuoteForm(forms.ModelForm):
    """
        a form to update a new quote object
    """
    class Meta:
        """
            Additional data about this form
        """
        model = Quote #which model to create
        fields = ['text', 'person']