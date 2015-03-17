from django.shortcuts import render
from django.views.generic import ListView
from address.models import Address
# Create your views here.
class AddressList(ListView):
    model = Address
