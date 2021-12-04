from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'required' : '', 'class' : 'form-control'}))
	last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'required' : '', 'class' : 'form-control'}))
	# age = forms.IntegerField(widget=forms.NumberInput(attrs={'max' : '100', 'min' : '0', 'required' : ''}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'required' : '', 'class' : 'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class' : 'form-control'})
		self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['password2'].widget.attrs.update({'class' : 'form-control'})


class AccountForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')

		widgets = {
          'username' : forms.TextInput(attrs={'class' : 'form-control'}),
          'email' : forms.EmailInput(attrs={'required' : '', 'class' : 'form-control'}),
          'first_name' : forms.TextInput(attrs={'required' : '', 'class' : 'form-control'}),
          'last_name' : forms.TextInput(attrs={'required' : '', 'class' : 'form-control'}),

        }