#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.template import loader,Context
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


@csrf_exempt
def login(request):
    username = request.POST.get('username',None)
    if username:
        request.session['username'] = username
        return render(request,'login.html',{'username':username})
    return render(request,'login.html')

@csrf_exempt
def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponseRedirect('/login/')

def output(request,filename):
    address = [(1,2),('一','二')]
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment;filename={0}'.format(filename)
    t = loader.get_template('csv.html')
    c = Context({
            'data':address,
        })
    response.write(t.render(c))
    return response

@csrf_exempt
def add(request):
    if request.POST.get('one',None):
        a = int(request.POST['one'])
        b = int(request.POST['two'])
    else:
        a=0
        b=0
    return render(request,'add.html',{'a':a,'b':b,'sum':a+b})


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
