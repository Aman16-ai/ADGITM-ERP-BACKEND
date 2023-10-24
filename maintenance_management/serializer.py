from rest_framework import serializers
from .models import MaintenanceIssue
from accounts.models import UserAccount

class MaintenanceIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceIssue
        exclude = ('created_by',)

    def create(self, validated_data):
        user = self.context['request'].user
        obj = MaintenanceIssue(created_by = user, **validated_data)
        obj.save()
        return obj
    

class MaintenanceIssueStatusAndCountSerializer(serializers.Serializer):
    status = serializers.CharField()
    count = serializers.IntegerField()