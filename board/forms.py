from django.forms import ModelForm

from .models import Cont

class ContForm(ModelForm):
    class Meta:
        model = Cont
        fileds = ('title', 'textContent')
# Create your views here.