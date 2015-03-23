from django.shortcuts import render
from django.http import HttpResponse
from postgresqltest.models import Order,Address 
from django.db import transaction,connection
# Create your views here.
import time
class autoclose(object):
    def __init__(self, f=None):
        self.f = f

    def __call__(self, *args, **kwargs):
        with self:
            return self.f(*args, **kwargs)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_info, tb):
        from django.db import close_connection
        close_connection()
        return exc_type is None

def create_order(request):
    address = Address(street_address="1112 E Broad St", city="Westfield", state="NJ", zipe="07090")
    address.save()
    order = Order(customer_name="Gomez Addams", shipping_address=address)
    order.save()
    return HttpResponse(u"create: " + unicode(order))

def show_order(request,order_id):
    order = Order.objects.get(pk=order_id)
    return HttpResponse(unicode(order))

#@auto_close
def show_order_all(request):
#    import logging
#    logger = logging.getLogger(__name__)
#    logger.error("now select!")
    order = Order.objects.all()
    n = len(order)
    for i in xrange(10):
#        logger.error("now insert",i)
        time.sleep(0.1)
        create_order(request)
#    response = u' '.join([unicode(o) for o in order])
    return HttpResponse(u"ok")
