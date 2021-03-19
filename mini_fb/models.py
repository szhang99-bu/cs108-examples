from django.db import models

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