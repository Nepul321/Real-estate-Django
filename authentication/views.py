from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import (
  login_required
)
from .decorators import (
  not_active_user,
  unauthenticated_user,
)
from .forms import (
  CreateUserForm,
  AccountForm
)
from django.core.mail import send_mail

from .models import UserKey

from django.contrib.auth import update_session_auth_hash
from src.settings import EMAIL_HOST_USER
from django.contrib.auth.forms import PasswordChangeForm

current_host = "http://localhost:8000"

@unauthenticated_user
def SignUpView(request):
	template = "signup.html"
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		results = User.objects.filter(email=request.POST['email'])
		if results:
			return redirect('signup')
		else:
			if form.is_valid():
						form.save()
						user = User.objects.get(username=request.POST['username'])
						user_key = UserKey.objects.create(
							user=user
						)
						user_key.save()
						user.is_active = False
						user.save()
						subject = "Verify your email"
						message = f"Thanks for signing up. \n Verify your email - {current_host}/activate-account/{user_key.key}/"
						email_from = EMAIL_HOST_USER
						recipient_list = [user.email, ]
						send_mail(subject, message, email_from, recipient_list)
						template2 = "email_sent.html"
						context2 = {}
						return render(request, template2, context2)
	context = {
      'form' : form,
	}

	return render(request, template, context)

@login_required
def AccountView(request):
	template = "account.html"
	user = request.user
	form = AccountForm(instance=request.user)
	if request.method == "POST":
		form = AccountForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('account')
	context = {
      'form' : form,
	}

	return render(request, template, context)

@login_required
def PasswordView(request):
	template = "password.html"
	form = PasswordChangeForm(user=request.user)
	if request.method == "POST":
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('account')

	context = {'form' : form}
	return render(request, template, context)

def DeleteAccountView(request):
	  template = "delete.html"
	  if request.method == "POST":
	  	 user = User.objects.get(id=request.user.id)
	  	 user.delete()
	  	 return redirect('home')
	  context = {

	  }

	  return render(request, template, context)

@not_active_user
def ActivateAccountView(request, token):
	try:
		user = UserKey.objects.get(key=token)
		user.activated = True
		user.save()
		user.user.is_active = True
		user.user.save()
	except:
		return redirect('/')
	template = 'account-activated.html'
	context = {}
	return render(request, template, context)