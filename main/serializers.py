from rest_framework import serializers
from .models import Requirements,Donations,NGO,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email","mobile_number","address","city","pincode","is_NGO","is_Donor","credit",]

class NGOSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,read_only=True)
    class Meta:
        model = NGO
        fields = ["id","user","organisation_name","registration_no","certificate","website_link","is_verified",]

class RequirementsSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Requirements
        fields = ["id","created_by","equipments","quantity","description","reason","required_by","additional",]

class DonationsSerializer(serializers.ModelSerializer):
    donated_by = UserSerializer(many=False,read_only=True)
    equipment_donated = RequirementsSerializer(many=False,read_only=True)

    class Meta:
        model = Donations
        fields = ["id","donated_by","equipment_donated","quantity_donated","request_made","donated_on","validated"]