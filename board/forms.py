from django.forms import ModelForm
from django.forms.widgets import TextInput

from .models import Comments

class ContForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('Name', 'Text')
        
        widgets = {'Text': TextInput(attrs={'width':10, 'height':3})}
# Create your views here.
