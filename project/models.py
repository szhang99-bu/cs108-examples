from django.db import models
from django.urls import reverse
from django.db.models import Q

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
    
    def get_all_bids(self):
        """
            will obtain and return all the bids for this item
        """
        
        bids = Bid.objects.filter(Q(sold=False) & Q(product=self)).order_by("-price")
        return bids
    
    def get_all_asks(self):
        """
            will obtain and return all the bids for this item
        """
        
        asks = Ask.objects.filter(Q(sold=False) & Q(product=self)).order_by("price")
        return asks
    
    def get_highest_bid(self):
        """
            Getting the higest bid from the query set
        """
        high_bid = Bid.objects.filter(Q(sold=False) & Q(product=self)).order_by("-price").first()
        return high_bid
    
    def get_lowest_ask(self):
        """
            Getting the higest bid from the query set
        """
        low_ask = Ask.objects.filter(Q(sold=False) & Q(product=self)).order_by("price").first()
        return low_ask

    def get_all_sold(self):
        """
            Getting all recent sold products.
        """
        bid_sold = Bid.objects.filter(Q(sold=True) & Q(product=self))
        ask_sold = Ask.objects.filter(Q(sold=True) & Q(product=self))
        total_sale = ask_sold.union(bid_sold)
        return total_sale




    

# class User(models.Model):
#     """
#         model the data attributes for each user that are using the website
#     """
#     first_name = models.TextField(blank=True)
#     last_name = models.TextField(blank=True)
#     address = models.TextField(blank=True)
#     email = models.TextField(blank=True)
#     phone_number = models.TextField(blank=True)

#     def __str__(self):
#         """
#             Return a string representation of the name city and email
#         """
#         return f'{self.first_name} {self.last_name} - {self.email} {self.phone_number} - {self.address}'
    
#     # def get_absolute_url(self):
#     #     """
#     #         Provide a url to show this object
#     #     """
#     #     return ''

class Ask(models.Model):
    """
        model the data attributes for each asks (selling price)
    """
    product = models.ForeignKey(ComputerParts, on_delete = models.CASCADE)
    list_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    sold = models.BooleanField(default=False)
    email = models.TextField(blank=True)
    phone_number = models.TextField(blank=True)

    def __str__(self):
        """
            Return a string representation of the name city and email
        """
        return f'Selling {self.product} - ${self.price} - {self.list_date}'


class Bid(models.Model):
    """
        model the data attributes for each bids (buying price)
    """
    product = models.ForeignKey(ComputerParts, on_delete = models.CASCADE)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    list_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    sold = models.BooleanField(default=False)
    email = models.TextField(blank=True)
    phone_number = models.TextField(blank=True)

    def __str__(self):
        """
            Return a string representation of the name city and email
        """
        return f'Selling {self.product} - ${self.price} - {self.list_date}'
    
    
