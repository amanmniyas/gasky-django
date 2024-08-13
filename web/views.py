from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from web.forms import ContactForm


def index(request):
    return render(request, 'web/index.html', {'current_page': 'index', 'title': 'Home'})


def about(request):
    return render(request, 'web/about.html', {'current_page': 'about', 'title': 'About Us'})


def services(request):
    return render(request, 'web/services.html', {'current_page': 'services', 'title': 'Our Services'})


def products(request):
    return render(request, 'web/products.html', {'current_page': 'products', 'title': 'Our Products'})


def contact(request):
    return render(request, 'web/contact.html', {'current_page': 'contact', 'title': 'Contact Us'})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        formset = ContactForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                f'New Contact Form Submission: {subject}',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                email,
                ['amanmniyas@gmail.com'],  # Admin email
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')  # Redirect to same page after submission
    else:
        formset = ContactForm()
    
    return render(request, 'contact.html', {'form': formset})