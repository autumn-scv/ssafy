from rest_framework import serializers
from .models import Artists

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['id', 'name', 'agency', 'debut_date', 'is_group']