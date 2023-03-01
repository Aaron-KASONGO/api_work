from rest_framework import serializers

from .models import Groupe


class GroupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groupe
        fields = ('name', 'date',)