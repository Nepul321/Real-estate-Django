from .models import Inquiry
from django import forms

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ("phone", "message")

        widgets = {
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control'}),
        }
