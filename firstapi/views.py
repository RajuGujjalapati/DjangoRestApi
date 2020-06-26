from django.shortcuts import render
from rest_framework import viewsets
from .models import Language,Paradigm,Programmer,Activity
from .serializers import LanguageSerailizer,ProgrammerSerializer,ParadigmSerializer, ActivitySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerailizer

class ParadigmviewwSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
        
class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    def some(request):
        return Response(request,{"jdsdf":"sdsadfsa"})
