from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Cont


def index(request):
    cont = Cont.objects.order_by('-published')
    context = {'cont': cont}
    return render(request, 'board/index.html', context)

def by_conf(request, rubric_id):
    cont = Cont.objects.order_by('-published')
    context = {'cont': cont, 'conf': rubric_id}
    return render(request, 'board/index.html', context)
# Create your views here.
