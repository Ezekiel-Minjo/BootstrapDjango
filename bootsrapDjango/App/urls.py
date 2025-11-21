from django.urls import path
from App import views

urlpatterns = [
    path('', views.home, name= 'index'),
    path('about/', views.about, name= 'about'),
    path('service/', views.service, name= 'service'),
    path('donation/', views.donation, name= 'donation'),
    path('event/', views.event, name= 'event'),
    path('feature/', views.feature, name= 'feature'),
    path('team/', views.team, name= 'team'),
    path('testimonial/', views.testimonial, name= 'testimonial'),
    path('contact/', views.contact, name= 'contact'),
]