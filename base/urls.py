from django.urls import path
from .views import (
    HomeView,
    PropertyDetailView,
    InquiryCreateView,
    DashboardView,
    DeleteInquiryView,
    AboutView
)

urlpatterns = [
   path('', HomeView, name="home"),
   path('properties/<str:pk>/', PropertyDetailView, name="details"),
   path('make-inquiry/properties/<str:pk>/', InquiryCreateView, name="create-contact"),
   path('dashboard/', DashboardView, name="dashboard"),
   path('delete-contact/<str:id>/', DeleteInquiryView, name="delete-contact"),
   path('about/', AboutView, name="about")
]