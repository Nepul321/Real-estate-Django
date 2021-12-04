from django.contrib import admin
from .models import (
    Inquiry,
    Listing,
    Realtor
)

admin.site.register(Inquiry)
admin.site.register(Listing)
admin.site.register(Realtor)