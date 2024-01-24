from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Ghost, Evidence


class EvidencesSerializer(serializers.ModelSerializer):
    ghosts = serializers.StringRelatedField(many=True)

    class Meta:
        model = Evidence
        fields = '__all__'


class GhostsSerializer(serializers.ModelSerializer):
    evidences = serializers.StringRelatedField(many=True)

    class Meta:
        model = Ghost
        fields = '__all__'

