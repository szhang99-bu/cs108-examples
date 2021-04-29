from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ComputerParts)
# admin.site.register(User)
admin.site.register(Ask)
admin.site.register(Bid)