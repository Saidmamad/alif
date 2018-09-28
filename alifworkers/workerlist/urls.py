from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^$', views.index, name='index'), #This is our first url pattern or first route
    #url(r'^$', views.tours, name='tours.html')
    url(r'^$', views.homepage),
];

