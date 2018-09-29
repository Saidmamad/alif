from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from workerlist.models import Workers, Education, Address, Position
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from workerlist import views
from django.conf import settings

app_name = 'workerlist'

urlpatterns = [
    url(r'^$', views.WorkersView.as_view()),
    url(r'^worker_details/(?P<id>[-\w+]+)/$', views.details, name='worker_details'),
];

