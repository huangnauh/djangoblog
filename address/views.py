#coding=utf-8
from django.shortcuts import render
from django.views.generic import ListView
from address.models import Address
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import io
import unicodecsv
import sys

# Create your views here.
class AddressList(ListView):
    model = Address
    paginate_by = 10

@csrf_exempt
def upload(request):
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


