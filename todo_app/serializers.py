from rest_framework import serializers

from .models import Groupe, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'date')

class GroupeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=2, max_length=30)
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Groupe
        fields = ('id', 'name', 'date', 'tasks',)
    
    def get_tasks(self, instance):
        items = Task.objects.filter(groupe=instance)
        return TaskSerializer(items, many=True).data