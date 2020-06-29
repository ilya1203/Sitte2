from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .forms import ContForm
from .models import Comments


def index(request, lang, conf):
    f = open('visit.txt', 'r')
    v = int(f.read())
    v += 1
    f.close()
    f = open('visit.txt', 'w')
    f.write(str(v))
    f.close()
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
    return render(request, 'board/index.html', {'vis': v,'lang':lang, 'form':ContForm, 'comm':comm, 'conf': conf})


