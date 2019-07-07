<<<<<<< HEAD
from django.forms import ModelForm, TextInput
from .models import City 

class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
=======
from django.forms import ModelForm, TextInput
from .models import City 

class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
>>>>>>> first commit
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}