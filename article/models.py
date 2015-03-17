from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    catagory = models.CharField(max_length=50,blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True)

    def get_absolute_url(self):
        path = reverse("detail",kwargs={'id':self.id})
        return "http://54.191.239.9:8000%s" % path

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-datetime']

