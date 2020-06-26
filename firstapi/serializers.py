from rest_framework import serializers
from .models import Language, Paradigm, Programmer

class LanguageSerailizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id','name','url')
class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields  = ('id', 'name')
class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'name')