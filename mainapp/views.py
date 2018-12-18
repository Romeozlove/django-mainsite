from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        'current_date': datetime.now(),
        'title': 'Home'
    }
    return render(request, 'mainapp/index.html', context)
