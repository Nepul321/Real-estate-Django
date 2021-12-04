from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import Inquiry, Listing, Realtor
from .filters import ListingFilter
from django.urls import reverse
from .forms import InquiryForm
from django.contrib.auth.decorators import login_required

def HomeView(request):
	template = "home.html"
	listings = Listing.objects.filter(is_published=True)
	myfilter = ListingFilter(request.GET, queryset=listings)
	listings = myfilter.qs
	context = {
		'results' : listings,
		'filter' : myfilter,
	}

	return render(request, template, context)

def PropertyDetailView(request, pk):
	template = "property_details.html"
	try:
		property = Listing.objects.get(id=pk)
	except:
		return HttpResponse("Property does not exist")
	context = {
          'property' : property,
	}

	return render(request, template, context)

@login_required
def InquiryCreateView(request, pk):
	template = "inquirycreate.html"
	property = Listing.objects.get(id=pk)
	contacts = Inquiry.objects.filter(listing=property)
	inquiries = contacts.filter(user=request.user)
	if not inquiries:
		form = InquiryForm()
		if request.method == "POST":
			phone = request.POST.get("phone")
			message = request.POST.get("message")
			inquiry = Inquiry.objects.create(
				listing=property,
				user=request.user,
				phone=phone,
				message=message
			)
			inquiry.save()
			return HttpResponseRedirect(reverse('details', args=[str(property.id)]))
		context = {
			'form' : form,
			'property' : property,
		}

		return render(request, template, context)
	else:
		return redirect('dashboard')

@login_required
def DashboardView(request):
	template = "dashboard.html"
	contacts = Inquiry.objects.filter(user=request.user)
	context = {
        'contacts' : contacts,
	}
	
	return render(request, template, context)
@login_required
def DeleteInquiryView(request, id):
	if request.method == "POST":
		inquiry = Inquiry.objects.filter(id=id)
		if inquiry.first().user == request.user:
			inquiry.delete()
			return redirect('dashboard')
		else:
			return redirect('dashboard')
	else:
		return redirect('dashboard')

def AboutView(request):
	template = "about.html"
	realtors = Realtor.objects.all()
	best = realtors.filter(is_mvp=True).first()
	if best:
		context = {
			'realtors' : realtors,
			'best' : best,

		}
	else:
		context = {
			'realtors' : realtors,

		}
		

	return render(request, template, context)