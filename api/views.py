from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework import permissions

from api.serializers import UserSerializer,PopulationSerializer
from population.models import Worldpopulation


class UserView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,*args, **kwargs):
        user=request.user
        qs=User.objects.filter(username=user)
        serializer=UserSerializer(qs,many=True)
        return Response(data=serializer.data)
    
class PopulationView(ModelViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=PopulationSerializer
    queryset=Worldpopulation.objects.all()
    