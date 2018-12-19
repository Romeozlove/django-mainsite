from django.shortcuts import render
from datetime import datetime
from .models import Article


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
    db_populate()
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'current_date': datetime.now(),
        'title': 'News'
    }
    return render(request, 'mainapp/news.html', context)

def db_populate():
    if Article.objects.count() == 0:
        Article(title='first item', content='this is the first db content').save()
        Article(title='second item', content='this is the second db content').save()
        Article(title='third item', content='this is the third db content').save()
