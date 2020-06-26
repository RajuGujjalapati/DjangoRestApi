from rest_framework import serializers
from .models import Language, Paradigm, Programmer,Activity

class LanguageSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id','name','url','paradigm')
        #depth=1
        #use hyperlinked if u need to give seperate url for paradgm
        #If You  need just id, use modelSerializer
class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields  = ('id', 'name')
        depth =1
class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'name','languages')
        depth = 2
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','start_date','end_date', 'activity','start_date','end_date')
        depth = 2