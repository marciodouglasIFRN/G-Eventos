from django.http import HttpResponse
from django.shortcuts import render



# def promoter(request):
# 	return render(request,'promoter.html')

def register(request):
	return render(request,'register.html')

def login(request):
	return render(request,'login.html')