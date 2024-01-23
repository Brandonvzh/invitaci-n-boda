from django import forms
from . import models

class Guests_bride_form(forms.ModelForm):
    class Meta:
        model = models.Guests
        fields = ['identifier', 'num_guests_assigned']
        
        widgets = {'identifier': forms.TextInput(attrs = {'class': 'input-inv h-18 min-w-[20rem] rounded-lg border-white-500 indent-4 text-white-900 shadow-lg focus:outline-none focus:ring focus:ring-white-600', 'placeholder': 'Ingresar invitado', 'autocomplete': 'off'}),
                    'num_guests_assigned': forms.TextInput(attrs = {'class': 'input-asis h-18 min-w-[20rem] rounded-lg border-white-500 indent-4 text-white-900 shadow-lg focus:outline-none focus:ring focus:ring-white-600', 'placeholder': 'Ingresar cantida de invitados', 'autocomplete': 'off'}),}
        
class Guests_form(forms.ModelForm):
    class Meta:
        model = models.Guests
        fields = ['num_guests_selected', 'answer', 'guests_names', 'wish_text']
        
        
class SearchForm(forms.Form):
    code = forms.CharField(max_length = 6, required = False)
    
