from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from article.views import RSSFeed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','article.views.home'),
    url(r"^(?P<id>\d+)/$",'article.views.detail',name='detail'),
    url(r"^archive/$",'article.views.archive',name='archive'),
    url(r"^tag(?P<tag>\w+)/$",'article.views.search_tag',name='search_tag'),
    url(r"^feed/$",RSSFeed(),name='RSS'),
    url(r"^add/$",'article.views.add',name='add'),
    url(r"^csv/(?P<filename>\w+)/$",'article.views.output'),
    url(r"^login/$",'article.views.login',name='login'),
    url(r"^logout/$",'article.views.logout',name='logout'),
    url(r'^address/',include('address.urls')),
    url(r"^request-info/$","article.views.show_request",name="show_request"),
)
