from django.shortcuts import render
from rest_framework import viewsets
from .models import Language,Paradigm,Programmer
from .serializers import LanguageSerailizer,ProgrammerSerializer,ParadigmSerializer
class ModelViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerailizer

class ParadigmviewwSet(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
