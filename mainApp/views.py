from django.shortcuts import render
#from django.http import HttpResponse

def index(request):
	return render(request, 'mainApp/homePage.html')
# Create your views here.
def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['Если есть вопросы, задавай из по телефону', 
	'8800-555-35-35', 'example@mail.ru']})