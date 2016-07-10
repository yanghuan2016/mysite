from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blog_views


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blog_views.index, name='index'),
    url(r'^calendar', blog_views.calendar, name='calendar'),
]