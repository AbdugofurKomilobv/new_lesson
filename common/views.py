from django.shortcuts import render
from .models import *


def home_page(request): 
    news = News.objects.all()
    db = {
      "news":news,
      "title": "News title"


    }
    return render(request=request,template_name='index.html',context=db)