from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic.base import TemplateView
from workerlist.models import Workers, Education, Address, Position
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


class WorkersView(TemplateView):
    template_name = 'workerlist/index.html'

    def get(self, request):

        workers = Workers.objects.all()
        paginator = Paginator(workers, 3) # Show 3 workers per page
        page = request.GET.get('page')
        workers = paginator.get_page(page)
        args = {'workers':workers, } 
        return render(request, self.template_name, args )




def details(request, id):
    worker=Workers.objects.get(id=id)
    address = Address.objects.get(id=worker.id)
    position = Position.objects.get(worker_id=id)
    education = Education.objects.filter(worker_id = id)
    context = {
        'worker' : worker,
        'address': address,
        'education': education,
        'position': position,
    }

    return render(request, 'workerlist/details.html', context)

