from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
# Create your views here.

def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html',{'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,"post.html",{'post':post})

def archive(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archive.html',{'post_list':post_list})

def search_tag(request,tag):
    try:
        post_list=Article.objects.filter(catagory__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})
