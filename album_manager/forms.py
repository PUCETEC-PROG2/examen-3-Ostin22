from django import forms 
from .models import Discos, Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'})
        }
        
class DiscosForm(forms.ModelForm):
    class Meta:
        model = Discos
        fields = '__all__'
        widgets = {
            'genre' : forms.Select(attrs={'class': 'form-control'}),
            'year' : forms.NumberInput(attrs={'class': 'form-control'}),
            'artist' : forms.Select(attrs={'class': 'form-control'}),
            'picture' : forms.ClearableFileInput(attrs={'class': 'form-control'})
        }