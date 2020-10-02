from rest_framework import serializers
from .models import College, Vlogger, Vlogs, FAQs, Requests

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'

class VloggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vlogger
        fields = '__all__'
        
class VlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vlogs
        fields = '__all__'
        
class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQs
        fields = '__all__'
        
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'