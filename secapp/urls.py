
from django.urls import path
from secapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ourservices/', views.ourservices, name='ourservices'),
    path('ourteam/', views.ourteam, name='ourteam'),
    path('tovisit/', views.tovisit, name='tovisit'),
	path('dosto/', views.dosto, name='dosto'),
    path('famous/', views.famous, name='famous'),
    path('cities/', views.city, name='cities'),
	path('offers/', views.offers, name='offers'),
    path('services_details/<int:service_id>/', views.services_details, name='services_details'),  
    path('about/', views.about, name='about'),



    path('visa/', views.visa, name='visa'),
    path('health/', views.health, name='health'),
	# path('dosto/hi/', views.hi, name='hi'),
    path('guide/', views.guide, name='guide'),

    #Detils pages
    path('dosto_details/<int:dosto_id>/', views.dosto_details, name='dosto_details'),
    path('city_details/<int:city_id>/', views.city_details, name='city_details'),
    path('face_details/<int:fame_id>/', views.face_details, name='face_details'),
    path('offer_details/<int:offer_id>/', views.offer_details, name='offer_details'),

]
