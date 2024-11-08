from django import forms
from .models import Projet, Tache

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'description', 'date_debut', 'date_fin', 'statut']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['projet', 'titre', 'description', 'date_echeance', 'statut']
        widgets = {
            'date_echeance': forms.DateInput(attrs={'type': 'date'}),
        }


