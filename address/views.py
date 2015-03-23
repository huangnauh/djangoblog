#coding=utf-8
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from address.models import Address
from django.http import HttpResponseRedirect
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required
import io
import unicodecsv
import sys
from forms import LoginForm

# Create your views here.

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,"address/login.html",{"form":form,})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get("password",'')
            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return render(request,'home.html')
            else:
                return render(request,"address/login.html",{"form":form,"password_is_wrong":True})
        else:
            return render(request,"address/login.html",{"form":form,})





class AddressList(ListView):
    model = Address
    paginate_by = 10





@csrf_exempt
@staff_member_required
def upload(request):
    if request.user.username != 'huang':
        return render(request,"address/error.html",{"message":"未登录"})
    file = request.FILES.get('file',None)
    if file:
        buf = io.BytesIO(file.read().decode('GBK').encode('utf-8'))
        try:
            reader = unicodecsv.reader(buf,encoding='utf-8')
        except:
            return render(request,"address/error.html",{"message":"need a csv file!"}) 
        for row in reader:
            objs = Address.objects.filter(name=row[0])
            if not objs:
                obj = Address(name=row[0],gender=row[1],telphone=row[2],mobile=row[3])
            else:
                obj = objs[0]
                obj.gender = row[1]
                obj.telphone = row[2]
                obj.mobile = row[3]
            obj.save()
        return HttpResponseRedirect('/address/')
    return render(request,"address/error.html",{"message":"need a file!"})


