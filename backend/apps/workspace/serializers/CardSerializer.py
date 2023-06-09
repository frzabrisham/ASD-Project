from rest_framework import serializers

from apps.workspace.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'title', 'order', 'description']