from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.conf import settings
from django.views.generic.base import TemplateView
from workerlist.models import Workers, Education, Address, Position
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

def homepage(request):
    return render(request, 'workerlist/index.html')


class WorkersView(TemplateView):
    template_name = 'workerlist/index.html'

    def get(self, request):
        # form = CreateTourForm()
        workers = Workers.objects.all()
        address = Address.objects.all()
        position = Position.objects.all()
        # destination = Destination.objects.all()

        # print(destination)
        # dest = Tour.objects.filter(id = Destination_id)
        # destination2 = Destination.objects.filter(dest = Destination_id)

        paginator = Paginator(workers, 3) # Show 9 tours per page
        page = request.GET.get('page')
        workers = paginator.get_page(page)

        #users = User.objects.exclude(id=request.user.id) #v52     53 .all()
        args = {'workers':workers, 'address':address, 'positions': position, } #
        return render(request, self.template_name, args )

