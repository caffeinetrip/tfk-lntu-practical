# main_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'main_app/home.html', {'title': 'Головна сторінка'})

def about(request):
    return render(request, 'main_app/about.html', {'title': 'Про нас'})

def services(request):
    return render(request, 'main_app/services.html', {'title': 'Наші послуги'})

def projects(request):
    return render(request, 'main_app/projects.html', {'title': 'Наші проекти'})

def contact(request):
    return render(request, 'main_app/contact.html', {'title': 'Зв\'яжіться з нами'})