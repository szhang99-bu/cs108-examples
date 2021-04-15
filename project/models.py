from django.db import models
from django.urls import reverse

# Create your models here.

class ComputerParts(models.Model):
    """
        model the data attributes of computer parts that are selling
    """
    name = models.TextField(blank=True)
    year = models.TextField(blank=True)
    manufacturer = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        """
            Return a string representation of the name city and email
        """
        return f'{self.manufacturer} {self.name} - {self.year} {self.description} - ${self.original_price}'
    

class User(models.Model):
    """
        model the data attributes for each user that are using the website
    """
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    address = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone_number = models.TextField(blank=True)

    def __str__(self):
        """
            Return a string representation of the name city and email
        """
        return f'{self.first_name} {self.last_name} - {self.email} {self.phone_number} - {self.city}'

class Ask(models.Model):
    """
        model the data attributes for each asks (selling price)
    """
    product = models.ForeignKey(ComputerParts, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    list_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        """
            Return a string representation of the name city and email
        """
        return f'Selling {self.product} - ${self.price} @{self.list_date}'


class Bid(models.Model):
    """
        model the data attributes for each bids (buying price)
    """
    product = models.ForeignKey(ComputerParts, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    list_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        """
            Return a string representation of the name city and email
        """
        return f'Selling {self.product} - ${self.price} @{self.list_date}'
