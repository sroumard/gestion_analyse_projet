from django.urls import path
from . import views
from .views import ProjetListCreateView, KPIListCreateView, TacheListCreateView, KPIDetailView

urlpatterns = [
    path('projets/', views.projet_list, name='projet_list'),
    path('projets/<int:projet_id>/', views.projet_detail, name='projet_detail'),
    path('projets/nouveau/', views.projet_create, name='projet_create'),
    path('projets/<int:projet_id>/editer/', views.projet_edit, name='projet_edit'),
    path('projets/<int:projet_id>/taches/nouvelle/', views.tache_create, name='tache_create'),
    
    # API endpoints
    path('api/projets/', ProjetListCreateView.as_view(), name='api_projets'),
    path('api/taches/', TacheListCreateView.as_view(), name='api_taches'),
    path('api/kpis/', KPIListCreateView.as_view(), name='api_kpis'),
    path('api/kpis/<int:pk>/', KPIDetailView.as_view(), name='api_kpi_detail'),  # Nouveau point de terminaison pour un KPI spécifique

    # Nouvelles URLs pour les KPIs
    path('projets/<int:projet_id>/kpis/', views.kpi_list, name='kpi_list'),
    path('projets/<int:projet_id>/kpis/nouveau/', views.kpi_create, name='kpi_create'),
]


