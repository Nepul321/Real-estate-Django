import django_filters
from django_filters import CharFilter, NumberFilter
from .models import Listing

class ListingFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr='icontains', label="Title")
    city = CharFilter(field_name="city", lookup_expr='iexact', label="City")
    state = CharFilter(field_name="state", lookup_expr='iexact', label="State")
    price = NumberFilter(field_name="price", lookup_expr="lte", label="Price")
    description = CharFilter(field_name="description", lookup_expr="icontains", label="Key word")
    class Meta:
        model = Listing
        fields = ('title', 'city', 'state', 'price', 'bedrooms', 'bathrooms', 'garage','description')

