from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from .serializers import GroupeSerializer
from .models import Groupe


# Définir une Pagination sur la liste
class GroupePagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class GroupeList(ListAPIView):
    queryset = Groupe.objects.all()
    serializer_class = GroupeSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter) # Backend de filtre à utiliser
    filter_fields = ('id',) # Pour filtrer par l'id
    search_fields = ('name',) # Pour filtrer selon la recherche
    pagination_class = GroupePagination # Pour préciser le nombre de la pagination


    """
    def get_queryset(self): => pour filtrer tous les contenues du queryset
    """


class GroupeCreate(CreateAPIView):
    serializer_class = GroupeSerializer

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
            if len(name) == 0:
                raise ValidationError({'name': 'Ne doit pas être vide !'})
        except ValueError:
            raise ValidationError({ 'name': 'Un nom valide est requis !'})
        return super().create(request, *args, **kwargs)


class GroupeDestroy(DestroyAPIView):
    queryset = Groupe.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        groupe_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('groupe_data_{}'.format(groupe_id))
        return response
    

class GroupeRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Groupe.objects.all()
    lookup_field = 'id'
    serializer_class = GroupeSerializer

    def delete(self, request, *args, **kwargs):
        groupe_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('groupe_data_{}'.format(groupe_id))
        return response
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            groupe = response.data
            cache.set('groupe_data_{}'.format(groupe['id']), {
                'name': groupe['name'],
                'date': groupe['date']
            })
        return response
