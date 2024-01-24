from django.urls import path

from . import views

urlpatterns = [
    path('all_ghosts/', views.GhostsAPI.as_view(), name='all_ghosts'),
    path('all_evidences/', views.EvidencesAPI.as_view(), name='all_evidences'),
]
