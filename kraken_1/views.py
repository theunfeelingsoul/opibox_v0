from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.
def Index(request):
	return render(request,'kraken_1/index.html')