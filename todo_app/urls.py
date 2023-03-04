from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path('api/v1/groupes', api_views.GroupeList.as_view()),
    path('api/v1/groupes/new', api_views.GroupeCreate.as_view()),
    path('api/v1/groupes/<int:id>/delete', api_views.DestroyAPIView.as_view()),

    path('', views.index)
]
