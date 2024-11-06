from django.shortcuts import render, get_object_or_404
from .models import Projet


def projet_list(request):
    projets = Projet.objects.all()
    return render(request, 'gestion_projets/projet_list.html', {'projets': projets})

def projet_detail(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()
    return render(request, 'gestion_projets/projet_detail.html', {'projet': projet, 'taches': taches})


