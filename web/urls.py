from django.urls import path
from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('products/', views.products, name="products"),
    path('contact/', views.contact, name="contact"),
    path('contact-form/', views.contact_view, name="contact_view"),
]
