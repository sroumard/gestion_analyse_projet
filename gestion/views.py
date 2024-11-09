from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .forms import ProjetForm, TacheForm, KPIForm
from .models import Projet, KPI, Tache
from .serializers import ProjetSerializer, KPISerializer, TacheSerializer
# --- Vues basées sur les modèles pour les pages HTML ---

def projet_list(request):
    projets = Projet.objects.all()
    return render(request, 'gestion_projets/projet_list.html', {'projets': projets})

def projet_detail(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    taches = projet.taches.all()
    kpis = projet.kpis.all()  # Ajout des KPI liés au projet
    return render(request, 'gestion_projets/projet_detail.html', {'projet': projet, 'taches': taches, 'kpis': kpis})

def projet_create(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projet_list')
    else:
        form = ProjetForm()
    return render(request, 'gestion_projets/projet_create.html', {'form': form})

def projet_edit(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projet_detail', projet_id=projet.id)
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


# --- Vues API avec Django REST Framework ---

class ProjetListCreateView(generics.ListCreateAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

class TacheListCreateView(generics.ListCreateAPIView):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

class KPIListCreateView(generics.ListCreateAPIView):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer

class KPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KPI.objects.all()
    serializer_class = KPISerializer


def kpi_list(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    kpis = projet.kpis.all()
    return render(request, 'gestion_projets/kpi_list.html', {'projet': projet, 'kpis': kpis})

def kpi_create(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = KPIForm(request.POST)
        if form.is_valid():
            kpi = form.save(commit=False)
            kpi.projet = projet  # Lier le KPI au projet actuel
            kpi.save()
            return redirect('kpi_list', projet_id=projet.id)  # Rediriger vers la liste des KPIs
    else:
        form = KPIForm()
    return render(request, 'gestion_projets/kpi_create.html', {'form': form, 'projet': projet})