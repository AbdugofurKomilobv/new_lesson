from django.shortcuts import render
from .models import *


def home_page(request): 
    cat = Categories.objects.all()
    news = News.objects.all()
    db = {
      'cat' : cat,
      "news":news,
      "title": "News title"


    }
    return render(request=request,template_name='index.html',context=db)


def category_news(request,category_id):
        cat = Categories.objects.all()
        news = News.objects.filter(category_id=category_id)
        db = {
      'cat' : cat,
      "news":news,
      "title": "News title"


          }
        return render(request=request,template_name='home.html',context=db)

