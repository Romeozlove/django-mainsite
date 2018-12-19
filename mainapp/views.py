from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        'current_date': datetime.now(),
        'title': 'Home'
    }
    return render(request, 'mainapp/index.html', context)

def about(request):
    context = {
        'current_date': datetime.now(),
        'title': 'About'
    }
    return render(request, 'mainapp/about.html', context)

def news(request):
    context = {
        'current_date': datetime.now(),
        'title': 'News'
    }
    return render(request, 'mainapp/news.html', context)
