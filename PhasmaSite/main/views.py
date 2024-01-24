# Create your views here.
from django.db.models import Count
from rest_framework import generics

from .models import Ghost
from .serializers import *
from .serializers import GhostsSerializer


class GhostsAPI(generics.ListAPIView):
    """API для призраков"""
    serializer_class = GhostsSerializer

    def get_queryset(self):
        matching_evidences = self.request.GET.getlist('match')
        not_matching_evidences = self.request.GET.getlist('exclude')

        if matching_evidences and not_matching_evidences:
            return self.get_matching_and_not_matching(matching_evidences, not_matching_evidences)

        if matching_evidences:
            return self.get_matching(matching_evidences)

        if not_matching_evidences:
            return self.get_not_matching(not_matching_evidences)

        # Default case
        return Ghost.objects.order_by('pk').all()

    def get_matching(self, matching_evidences):
        return Ghost.objects.filter(
            evidences__id__in=matching_evidences
        ).annotate(
            match=Count('evidences', distinct=True)
        ).filter(
            match=len(matching_evidences)
        ).order_by('pk')

    def get_not_matching(self, not_matching_evidences):
        return Ghost.objects.exclude(
            evidences__id__in=not_matching_evidences
        ).order_by('pk')

    def get_matching_and_not_matching(self, matching_evidences, not_matching_evidences):
        return Ghost.objects.filter(
            evidences__id__in=matching_evidences
        ).exclude(
            evidences__id__in=not_matching_evidences
        ).annotate(
            match=Count('evidences', distinct=True)
        ).filter(
            match=len(matching_evidences)
        ).order_by('pk')


class EvidencesAPI(generics.ListAPIView):
    serializer_class = EvidencesSerializer

    def get_queryset(self):
        queryset = Evidence.objects.order_by('pk').all()
        return queryset
