from django.shortcuts import render
from .models import companies 
# Create your views here.

def companies(request):
	companies=companies.objects.all
	
	return redirect(request, 'quotes/about.html', {'companies':companies})
