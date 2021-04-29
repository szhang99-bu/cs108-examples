# files: mini_fb/urls.py
# description: direct URL requests to view functions

from django.urls import path
from .views import *

urlpatterns = [
    path('',ShowAllComputerParts.as_view(), name = 'show_all_computer_parts'),
    path('product/<int:pk>', ShowProductPageView.as_view(), name = 'show_computer_part_page'),
    # path('create_profile', CreateProfileView.as_view(), name = 'create_profile'),
    path('make_ask_page/<int:pk>', ShowMakeAskView.as_view(), name ="make_an_ask"),
    path('make_bid_page/<int:pk>',ShowMakeBidView.as_view(), name ="make_a_bid"),
    path('product/<int:pk>/make_ask_page/make_ask',create_ask, name ="make_an_ask_form"),
    path('product/<int:pk>/make_bid_page/make_bid',create_bid, name ="make_a_bid_form"),
    path('product/<int:product_pk>/update_bid/<int:bid_pk>', UpdateBidView.as_view(), name ="update_a_bid"),
    path('product/<int:product_pk>/update_ask/<int:ask_pk>', UpdateAskView.as_view(), name ="update_an_ask"),
    path('success/',ShowSuccessView.as_view(), name = 'congratulation'),
]