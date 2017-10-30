from django.shortcuts import render

# Create your views here.
def Home(request):

	return render(request,"home.html",{})

def Carriers(request):

	return render(request,"carriers.html",{})

def Shippers(request):

	return render(request,"shippers.html",{})

def Faq(request):

	return render(request,"faq.html",{})

def Team(request):

	return render(request,"team.html",{})

def Story(request):

	return render(request,"story.html",{})