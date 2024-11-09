from django import forms
from .models import KPI, Projet, Tache

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


class KPIForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = ['nom', 'valeur']  # Les champs que vous souhaitez inclure dans le formulaire

    def __init__(self, *args, **kwargs):
        super(KPIForm, self).__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'placeholder': 'Nom du KPI'})
        self.fields['valeur'].widget.attrs.update({'placeholder': 'Valeur du KPI'})