from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# pk_140be9f6adc047ffa2ee3a4d960a4c2d
# Create your views here.

def home(request):
	import requests
	import json
	if request.method=='POST':
		ticker=request.POST['ticker']

		api_request=requests.get("https://api.iex.cloud/v1/data/core/quote/" + ticker + "?token=pk_140be9f6adc047ffa2ee3a4d960a4c2d")
		
		try:
			api_u=json.loads(api_request.content)
			api=api_u[0] # unpack api list to dictionary


		except Exception as e:
			api="Error.."
		return render(request,'home.html',{'api': api}) 	
	else:
		return render(request,'home.html',{'ticker': "enter a ticker symbol above"})	
	
	

def about(request):
	return render(request,'about.html',{}) 


def add_stock(request):
	import requests
	import json

	if request.method=='POST':
		form= StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added!"))
			return redirect('add_stock')


	else:		
		ticker= Stock.objects.all()
		output=[]
		
		for ticker_item in ticker:
			api_request=requests.get("https://api.iex.cloud/v1/data/core/quote/" + str(ticker_item) + "?token=pk_140be9f6adc047ffa2ee3a4d960a4c2d")

			try:
				api_u=json.loads(api_request.content)
				api=api_u[0] # unpack api list to dictionary
				output.append(api)


			except Exception as e:
				api="Error.."


		return render(request,'add_stock.html',{'ticker':ticker, 'output':output}) 


def delete(request, stock_id):
	item= Stock.objects.get(pk= stock_id)
	item.delete()
	messages.success(request, ("Stock has been deleted!"))
	return redirect('add_stock')



