# files: quotes/urls.py
# description: direct URL requests to view functions

from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView

urlpatterns = [
    path('', RandomQuotePageView.as_view(), name = 'random'),
    path('all', HomePageView.as_view(), name = 'all_quotes'),
    path('quote/<int:pk>', QuotePageView.as_view(), name = 'quote'),

]