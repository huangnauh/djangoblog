from django.db import models

# Create your models here.
class Address(models.Model):
    street_address = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=2)
    zipe = models.CharField(max_length=5)

    def __unicode__(self):
        return self.street_address + u" " + self.city + u" " + self.state + u" " + self.zipe

class Order(models.Model):
    customer_name = models.CharField(max_length=80)
    shipping_address = models.ForeignKey(Address)

    def __unicode__(self):
        return u"order " + unicode(self.id) + u" going to " + \
                self.customer_name + u", " + unicode(self.shipping_address)


