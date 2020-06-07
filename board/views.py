from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .forms import ContForm
from .models import Comments



def index(request, lang):
    comm = Comments.objects.all()
    if request.POST:
        c = Comments()
        if ContForm(request.POST).is_valid:
            c.Name = request.POST['Name']
            c.Text = request.POST['Text']
            for i in comm:
                if c.Text == i.Text and c.Name == i.Name:
                    break
            else:
                c.save()
    return render(request, 'board/newDesign.html', {'lang':lang, 'form':ContForm, 'comm':comm})


def about(request, lang, conf):
    return render(request, 'board/about.html', {'lang':lang, 'conf': conf})
