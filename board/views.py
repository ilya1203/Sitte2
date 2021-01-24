from django.shortcuts import render

# Create your views here.
from .models import Works

def index(request, lang):

    return render(request, 'index.html', {'lang':lang})


def selectors(request, lang, select):
    
    if select == 'Works':
        obj = Works.objects.all()
        for b in range(len(obj)):
            if lang == 'ru':
                obj[b].title = str(obj[b].title).split('|')[0]
                obj[b].comment = str(obj[b].comment).split('|')[0]
            else:
                obj[b].title = str(obj[b].title).split('|')[-1]
                obj[b].comment = str(obj[b].comment).split('|')[-1]
    else:
        obj = []
    
    return render(request, 'select.html', {'lang':lang, 'selc': select, 'obj':obj})
