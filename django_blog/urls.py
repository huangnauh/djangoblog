from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','article.views.home'),
    url(r"^(?P<id>\d+)/$",'article.views.detail',name='detail'),
    url(r"^archive/$",'article.views.archive',name='archive'),
    url(r"^tag(?P<tag>\w+)/$",'article.views.search_tag',name='search_tag'),
)
