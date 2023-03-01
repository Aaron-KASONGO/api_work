from rest_framework.generics import ListAPIView
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



