from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from workerlist.models import Workers, Education, Address, Position
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #url(r'^$', views.index, name='index'), #This is our first url pattern or first route
    #url(r'^$', views.tours, name='tours.html')
    url(r'^$', views.WorkersView.as_view()),
];

