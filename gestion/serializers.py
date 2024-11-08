# gestion/serializers.py
from rest_framework import serializers
from .models import Projet, KPI , Tache

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = '__all__'

class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = '__all__'

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'
