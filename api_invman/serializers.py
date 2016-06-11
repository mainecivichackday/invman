import models

from rest_framework import serializers


class apiSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.api
        fields = (
            'id', 
            'name', 
            'created', 
            'last_updated', 
            'Keywords', 
            'Status', 
            'uuid', 
            'location', 
        )


