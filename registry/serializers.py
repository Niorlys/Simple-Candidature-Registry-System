from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *

__all__ = ['TechSerializer', 'CandidateSerializer','CandidateTechSerializer', 
                'GetCandidateSerializer', 'GetCandidateTechSerializer']

class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'




class CandidateTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTechs
        fields = '__all__'

    def create(self, validated_data):
        exists = CandidateTechs.objects.filter(tech__id=validated_data['tech'].id, 
                        candidate__candidate_id=validated_data['candidate'].candidate_id).exists()
        if exists:
            raise ValidationError("Already exists an assigment.")
        return super().create(validated_data)

# For readable display
class GetCandidateTechSerializer(serializers.ModelSerializer):
    tech = serializers.StringRelatedField()
    candidate = serializers.StringRelatedField()
    class Meta:
        model = CandidateTechs
        fields = '__all__'



class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ['techs']


# For readable display
class GetCandidateSerializer(serializers.ModelSerializer):
    techs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Candidate
        fields = '__all__'




