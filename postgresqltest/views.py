from django.shortcuts import render
from django.http import HttpResponse
from postgresqltest.models import Order,Address 
from django.db import transaction,connection
# Create your views here.



def create_order(request):
    address = Address(street_address="1112 E Broad St", city="Westfield", state="NJ", zipe="07090")
    address.save()
    order = Order(customer_name="Gomez Addams", shipping_address=address)
    order.save()
    return HttpResponse(u"create: " + unicode(order))

def show_order(request,order_id):
    order = Order.objects.get(pk=order_id)
    return HttpResponse(unicode(order))
