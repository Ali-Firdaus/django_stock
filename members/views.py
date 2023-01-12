from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_user(request):
	from companies.models import companies
	companies=companies.objects.all()

	if request.method=='POST':
	
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        return redirect('add_stock')
		        
	    else:
	        messages.success(request,("There was an error logging in, Try again.."))
	        return redirect('login')
		        
		
	else:
		return render (request, 'members/template/authenticate/login.html', {'companies':companies})


def logout_user(request):
	logout(request)
	messages.success(request,("you logged out.."))
	return redirect('home')


def register_user(request):
	from companies.models import companies
	companies=companies.objects.all()

	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request,("you are regsitered.."))
			return redirect('add_stock')

	else:
		form=UserCreationForm()	
	
	return render(request, 'members/template/authenticate/register_user.html', {'form':form,'companies':companies})