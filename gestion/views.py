
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProjetForm,TacheForm
from .models import Projet


# gestion_projets/views.py
from django.shortcuts import render, redirect
from .forms import ProjetForm
def projet_list(request):
    projets = Projet.objects.all()
    return render(request, 'gestion_projets/projet_list.html', {'projets': projets})

def projet_detail(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()
    return render(request, 'gestion_projets/projet_detail.html', {'projet': projet, 'taches': taches})



def projet_create(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projet_list')  # Redirection vers la liste des projets
    else:
        form = ProjetForm()
    return render(request, 'gestion_projets/projet_create.html', {'form': form})



def projet_edit(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            print(f"Projet ID: {projet.id}")  # Debugging line

           # return redirect('projet_list')  # Redirection vers la liste des projets
           # return redirect('projet_detail', projet_id=projet.id)
            return render(request, 'gestion_projets/projet_edit.html', {'projet': projet})

        

    else:
        form = ProjetForm(instance=projet)
    return render(request, 'gestion_projets/projet_edit.html', {'form': form})




def tache_create(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = TacheForm(request.POST)
        if form.is_valid():
            tache = form.save(commit=False)
            tache.projet = projet
            tache.save()
            return redirect('projet_detail', projet_id=projet.id)
    else:
        form = TacheForm()
    return render(request, 'gestion_projets/tache_create.html', {'form': form, 'projet': projet})



