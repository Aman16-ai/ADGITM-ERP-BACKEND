from rest_framework import serializers
from .models import MaintenanceIssue, MaintenanceType, MaintenanceIssueComment
from accounts.models import UserAccount
from departmenant_managnement.models import Department
class MaintenanceIssueSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    maintenanceType = serializers.PrimaryKeyRelatedField(queryset=MaintenanceType.objects.all())
    class Meta:
        model = MaintenanceIssue
        exclude = ('created_by',)

    def create(self, validated_data):
        user = self.context['request'].user
        obj = MaintenanceIssue(created_by = user, **validated_data)
        obj.save()
        return obj

class GetMaintenanceIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model =MaintenanceIssue
        fields="__all__"
        depth = 1

class MaintenanceIssueStatusAndCountSerializer(serializers.Serializer):
    status = serializers.CharField()
    count = serializers.IntegerField()


class MaintenanceTypeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceType
        fields = "__all__"


class MaintenaceIssueCommentSerializer(serializers.ModelSerializer):
    maintenanceIssue = serializers.PrimaryKeyRelatedField(queryset=MaintenanceIssue.objects.all())
    class Meta:
        model = MaintenanceIssueComment
        exclude = ("commented_by",)

    def create(self, validated_data):
        user = self.context['request'].user
        comment = MaintenanceIssueComment(commented_by=user,**validated_data)
        comment.save()
        return comment
    
class GetMaintenaceIssueCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceIssueComment
        fields = "__all__"
        depth = 1