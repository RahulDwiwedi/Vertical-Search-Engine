from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import mobile

# Create your views here.
def search(request):
	
	return render(request, 'search/search.html', {})


def result(request):
	if request.method=='POST':
		keyword=request.POST.get('key')
		
	all_mobile=mobile.objects.filter(title=keyword)
	return render(request, 'search/result.html', {'all_mobile':all_mobile,'keyword':keyword})