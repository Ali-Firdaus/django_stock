from django.shortcuts import render, redirect
from .models import Stock
from companies.models import companies
from django.contrib import messages
from .forms import StockForm
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.http import HttpResponse 
	
# pk_140be9f6adc047ffa2ee3a4d960a4c2d
# Create your views here.

def home(request):
	import requests
	import json
	from companies.models import companies
	companies=companies.objects.all()

	if request.method=='POST':
		ticker=request.POST['ticker']
				
		try:
			ticker=ticker.split()
			ticker=ticker[0]
			api_request=requests.get("https://api.iex.cloud/v1/data/core/quote/" + ticker + "?token=pk_140be9f6adc047ffa2ee3a4d960a4c2d")
			api_u=json.loads(api_request.content)
			api=api_u[0] # unpack api list to dictionary


		except Exception as e:
			api="Error.."
		return render(request,'home.html',{'api': api, 'companies':companies, 'ticker':ticker}) 	
	else:
		return render(request,'home.html',{'companies':companies,'ticker': "enter a ticker symbol above"})	
	
	
	

def about(request):
	from companies.models import companies
	companies=companies.objects.all()
	
	return render(request,'about.html', {'companies':companies}) 


def add_stock(request):
	import requests
	import json

	from companies.models import companies
	companies=companies.objects.all()
	
	user=request.user.id
	if request.method=='POST':
		info=request.POST
		ninfo=info.get('ticker')
		ninfo=ninfo.split()
		ninfo=ninfo[0]
		temp=request.POST.copy()
		temp['ticker']=ninfo
		ticker_list= Stock.objects.filter(owner=user)
		if ninfo not in ticker_list:

			request.POST=temp
			temp1=temp
			form= StockForm(temp1 or None)

			if form.is_valid():
				stock=form.save(commit=False)
				stock.owner= request.user
				stock.save()
				messages.success(request, ("Stock has been added!"))
				return redirect('add_stock')
		else: 
			messages.success(request, ("Stock is already in your portfolio!"))
			return redirect('add_stock')		

	else:		
		ticker= Stock.objects.filter(owner=user)
		output=[]
		
		for ticker_item in ticker:
			api_request=requests.get("https://api.iex.cloud/v1/data/core/quote/" + str(ticker_item) + "?token=pk_140be9f6adc047ffa2ee3a4d960a4c2d")

			try:
				api_u=json.loads(api_request.content)
				api=api_u[0] # unpack api list to dictionary
				output.append(api)


			except Exception as e:
				api="Error.."


		return render(request,'add_stock.html',{'ticker':ticker, 'output':output, 'companies':companies}) 


def delete(request, stock_id):
	item= Stock.objects.get(pk= stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted!"))
	return redirect('add_stock')


def companies(request):
	from companies.models import companies
	companies=companies.objects.all()
	return render(request, 'base.html', {'companies':companies})
