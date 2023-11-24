from rest_framework import serializers
from population.models import Worldpopulation
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class PopulationSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)

    class Meta:
        model=Worldpopulation
        fields="__all__"
    

