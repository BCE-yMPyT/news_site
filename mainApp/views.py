from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
	print("request to index")
	return render(request, 'mainApp/homePage.html')
# Create your views here.
def contact(request):
	print("request to index")
	return render(request, 'mainApp/contacts.html')