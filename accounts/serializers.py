from rest_framework import routers, serializers, viewsets
from .models import Profiles


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = '__all__'