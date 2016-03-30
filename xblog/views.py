# -*- coding:UTF-8 -*-
from django.shortcuts import render
from .models import NavigationBar,News

# Create your views here.

def index(request):
    navigations=NavigationBar.objects.all()
    news=News.objects.all()
    return render(request,'xblog/index.html',{"navs":navigations,"news":news})
