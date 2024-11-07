from django.urls import path
from . import views

urlpatterns = [
    path('projets/', views.projet_list, name='projet_list'),
    path('projets/<int:projet_id>/', views.projet_detail, name='projet_detail'),
    path('projets/nouveau/', views.projet_create, name='projet_create'),  # Nouvelle URL pour la création de projet
    path('projets/<int:projet_id>/editer/', views.projet_edit, name='projet_edit'),  # Nouvelle URL pour l'édition
    path('projets/<int:projet_id>/taches/nouvelle/', views.tache_create, name='tache_create'),  # URL pour créer une tâche

]

