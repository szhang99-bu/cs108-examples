from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    """
        model the data attributes of Facebook users
    """
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        """
            Return a string representation of the name city and email
        """
        return f'{self.first_name} {self.last_name} {self.city} {self.email}'
    
    def get_status_messages(self):
        """
            Return all message for this Person.
        """

        #use the object manager to filter Quotes by this person's pk:
        return StatusMessage.objects.filter(profile=self)
    
    def get_absolute_url(self):
        """
            Provide a url to show this object
        """
        # 'quote/<int:pk>'
        return reverse('show_profile_page', kwargs={'pk':self.pk})


class StatusMessage(models.Model):
    """
        model called StatusMessage, which will model the data attributes of Facebook status message.
    """
    timestamp = models.TextField(blank=True)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    
    def __str__(self):
        """
            Return a string reoresentation of this quote.
        """
        return f'{self.message} @ {self.timestamp}'