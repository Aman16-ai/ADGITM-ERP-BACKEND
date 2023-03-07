from rest_framework import serializers
from .models import UserAccount,Faculty
from .services.RegisterService import RegisterService

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ("groups","user_permissions","last_login")

    def create(self, validated_data):
        register_ser = RegisterService()
        return register_ser.createUser(validated_data)


class FacultySerializer(serializers.ModelSerializer):
    faculty_user = UserAccountSerializer()
    class Meta:
        model = Faculty
        fields = "__all__"
    

    def create(self, validated_data):
        user_val_data = validated_data.pop('faculty_user')
        user_ser = UserAccountSerializer(data = user_val_data)
        user = None
        faculty_result = None
        if user_ser.is_valid(raise_exception=True):
            user = user_ser.save()
        if user is not None:
            register_ser = RegisterService()
            faculty_result = register_ser.registerFaculty(user_data=validated_data,user=user)
        if user is not None and faculty_result is not None:
            return user
        else:
            return None
