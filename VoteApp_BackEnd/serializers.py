from rest_framework import serializers
from .models import *

class VoteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteInfo
        fields = ('code','caption','is_Active','added_by','date_Created','last_Updated')


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('code','caption','icon', 'desc', 'remk','is_Active','added_by', 'date_Created', 'last_Updated')


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ('code','caption','is_Active','added_by','date_Created','last_Updated')

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('code','caption',  'Division', 'is_Active','added_by','date_Created','last_Updated')


class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upazila
        fields = ('code','caption',  'District', 'Division', 'is_Active','added_by','date_Created','last_Updated')

class UnionCouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnionCouncil
        fields = ('code','caption', 'Upazila', 'District', 'Division', 'is_Active','added_by','date_Created','last_Updated')

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = ('first_Name','last_Name', 'nid', 'password', 'contact_No', 'email','marital_Status','sex',
                  'Division','District', 'Upazila', 'UnionCouncil', 'voter_area', 'remk','is_Active','added_by','date_Created','last_Updated')



class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('caption','Party', 'VoteInfo', 'User', 'Voter', 'remk','is_Active','added_by','date_Created','last_Updated')


class VoteCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteCalculation
        fields = ('code','VoteInfo', 'Candidate', 'User', 'is_Active','added_by', 'date_Created','last_Updated')

class VoteWiseVoterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteWiseVoterList
        fields = ('VoteInfo', 'Voter', 'nid', 'tokenNumber','added_by', 'date_Created','last_Updated')
