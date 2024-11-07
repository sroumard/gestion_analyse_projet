from django import forms
from .models import Projet
from .models import Tache

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'description', 'date_debut', 'date_fin', 'statut']


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['projet', 'titre', 'description', 'date_echeance', 'statut']

