from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

class RSSFeed(Feed):
    title = "RSS Feed"
    link = "/feed/"
    description = "RSS Feed"
    def items(self):
        return Article.objects.order_by('-datetime')
    
    def item_title(self,item):
        return item.title
    
    def item_pubdate(self,item):
        return item.datetime

    def item_description(self, item):
        return item.content



def home(request):
    posts = Article.objects.all()
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
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
