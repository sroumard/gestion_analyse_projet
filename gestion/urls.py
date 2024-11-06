from django.urls import path
from . import views

urlpatterns = [
    path('projets/', views.projet_list, name='projet_list'),
    path('projets/<int:projet_id>/', views.projet_detail, name='projet_detail'),
]

