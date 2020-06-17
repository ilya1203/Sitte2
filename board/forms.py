from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Comments

class ContForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('Name',  'Text')
        
       
# Create your views here.
