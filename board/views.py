from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Cont, Rubric
from .forms import ContForm

class ContCreateView(CreateView):
    template_name = 'board/index.html'
    form_class = ContForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = {'conf': 'adds'}
        context['rubric'] = 'index'
        cc2 = {**context, **x} 
        return cc2

def index(request):
    cont = Cont.objects.order_by('-published')
    context = {'cont': cont}
    return render(request, 'board/index.html', context)

def by_conf(request, rubric_id):
    cont = Cont.objects.order_by('-published')
    
    context = {'cont': cont, 'conf': rubric_id}
    return render(request, 'board/index.html', context)
# Create your views here.
