from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from .models import Bottom
from .models import Last
from .models import Offers
from .models import Services
from .models import Dost, City, Famous

def index(request):
	return render (request,'secapp/index.html')

def home(request):
	offers=Offers.objects.all()
	services=Services.objects.all()
	bottoms=Bottom.objects.all()
	context={
	'title': ' الرئيسية',
	'offers': offers,
	'services': services, 
	'bottoms': bottoms,
	}
	return render(request,'secapp/home.html', context)

def ourservices(request):
	services=Services.objects.all()
	context = {
	'title': 'خدمات' ,
	'services': services ,
	}
	return render(request, 'secapp/ourservices.html', context)


def offers(request):
	offers=Offers.objects.all()
	context ={
	'title': 'عروض' ,
	'offers': offers ,
	}
	return render(request, 'secapp/offers.html', context)

def ourteam(request):
	return render(request,'secapp/ourteam.html')

def tovisit(request):
	bottoms=Bottom.objects.all()
	context ={
	'title': 'روسيا' ,
	'bottoms': bottoms ,
	}
	return render(request, 'secapp/tovisit.html', context)

def dosto(request):
	dosts=Dost.objects.all()
	return render(request,'secapp/dosto.html', {'dosts': dosts})

def city (request):
	cities = City.objects.all()
	context = {
		'cities': cities,
		'title': 'مدن',
	}
	return render(request, 'secapp/cities.html', context)

def famous (request):
	fames = Famous.objects.all()
	context = {
		'fames': fames,
		'title': 'شخصيات',
	}
	return render(request, 'secapp/famous.html', context)

def about(request):
	context={
		'title': ' من نحن'
	}
	return render (request,'secapp/about.html', context)


def hi(request):
	return render(request,'secapp/hi.html')

def health(request):
	context={
		'title': ' السفر للعلاج '
	}
	return render(request,'secapp/health.html', context)

def guide(request):
	return render(request,'secapp/guide.html')

def visa(request):
	return render(request,'secapp/visa.html')


#details

def offer_details(request, offer_id):
	offer = get_object_or_404(Offers, pk=offer_id)
	context = {
	'title': offer ,
	'offer': offer ,
	}
	return render(request, 'secapp/offer_details.html', context)


def services_details(request, service_id):
	service = get_object_or_404(Services, pk=service_id)
	context ={
	'title': service ,
	'service': service ,
	}
	return render(request, 'secapp/services_details.html', context)

def dosto_details(request, dosto_id):
	dost = get_object_or_404(Dost, pk=dosto_id)
	context = {
	'title': dost ,
	'dost': dost ,
	}
	return render(request, 'secapp/dosto_details.html', context)


def city_details(request, city_id):
	city = get_object_or_404(City, pk=city_id)
	context = {
	'title': city ,
	'city': city ,
	}
	return render(request, 'secapp/city_details.html', context)

def face_details(request, fame_id):
	fame = get_object_or_404(Famous, pk=fame_id)
	context = {
	'title': fame ,
	'fame': fame ,
	}
	return render(request, 'secapp/face_details.html', context)
