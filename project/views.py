from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.

class ShowAllComputerParts(ListView):
    """
        Show a listing of all the Computer Parts
    """
    model = ComputerParts #restieve Quote objects from teh database
    template_name = "project/show_all_computer_parts.html"
    context_object_name = "parts"

