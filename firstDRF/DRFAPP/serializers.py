from rest_framework import serializers

# Create your models here.
# from DRFAPP.models import Patient


class PatientSerializer(serializers.Serializer):
    USER_ID = serializers.CharField(max_length=30)
    TIMESTAMP = serializers.DateTimeField()
    AVG_HR = serializers.FloatField()
    MAX_HR = serializers.FloatField()
    MIN_RR = serializers.FloatField()
    AVG_RR = serializers.FloatField()
