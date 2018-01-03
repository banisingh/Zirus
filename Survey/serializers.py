from rest_framework import serializers
from Survey.models import Survey


class SurveySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created = serializers.DateTimeField()
    responses = serializers.JSONField()

    def create(self, validated_data):
        """
        Create and return a new Article instance,
        given the validated data.
        """

        return Survey.objects.create(**validated_data)