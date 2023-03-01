from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path('api/v1/groupes', api_views.GroupeList.as_view()),

    path('', views.index)
]
