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
    friends = models.ManyToManyField("self")

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
    
    def get_friends(self):
        """
            get all friends for each profile
        """ 
        return self.friends.all()

    def get_news_feed(self):
        """
            will obtain and return the news feed items.
        """
        # news = StatusMessage.objects.filter(profile__friends= self.friends).order_by("-timestamp")
        news = StatusMessage.objects.filter(profile__in = self.get_friends())
        news_self = StatusMessage.objects.filter(profile = self)

        total_news = news | news_self.order_by("-timestamp")
        return total_news
    
    def get_friend_suggestions(self):
        """
        suggest friends to add for users.
        """

        possible_friends = Profile.objects.exclude(pk__in= self.get_friends())
        return possible_friends


class StatusMessage(models.Model):
    """
        model called StatusMessage, which will model the data attributes of Facebook status message.
    """
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    
    def __str__(self):
        """
            Return a string reoresentation of this quote.
        """
        return f'{self.profile}" - {self.message} - {self.timestamp}'