from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *arg, **kwargs):
	# return HttpResponse("<h1>Hello world!</h1>")
	return render(request, "home.html", {})

def uwu_view(request, *arg, **kwargs):
	# return HttpResponse("<h2>uwu~!</h2>")
	return render(request, "uwu.html", {})

def test_view(request, *arg, **kwargs):
	return render(request, "test.html", {})