from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import datetime
# Create your views here.

def home_view(request, *arg, **kwargs):
	# return HttpResponse("<h1>Hello world!</h1>")
	return render(request, "home.html", {})

def uwu_view(request, *arg, **kwargs):
	BASEDIR = Path(__file__).resolve().parent
	akali = Path.joinpath(BASEDIR, 'akali.jpg')
	my_context = {
		"my_name": "art",
		"my_number": 69,
		"my_list": ["this", "is", "super", "cool"],
		"my_tuple": ("oh", "no"),
		"my_akali": akali,
		"my_html": "<h1>waht the fcuk is going on</h1>",
		"my_date": datetime.date(
			year = 2025,
			month = 1,
			day = 1
		),
	}
	return render(request, "uwu.html", my_context)

def test_view(request, *arg, **kwargs):
	return render(request, "test.html", {})