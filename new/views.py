from django.shortcuts import render

from .models import Nns
from .models import Rubric

def index(request):
    nns = Nns.objects.order_by('-published')
    sear = 'Поиск'
    rubrics = Rubric.objects.all()
    context = {'nns': nns, 'srr': sear, 'rubric': rubrics}
    return render(request, 'new/index.html', context)

def by_rubric(request, rubric_id):
    nns = Nns.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
   
    context = {'nns': nns, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'new/by_rubric.html', context)
