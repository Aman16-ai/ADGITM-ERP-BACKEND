from rest_framework import serializers
from .models import UserAccount,Faculty
from .services.RegisterService import RegisterService
from departmenant_managnement.models import Department
from .services.EmailService import EmailService
from .tasks import send_email_task
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        exclude = ("groups","user_permissions","last_login")

    def create(self, validated_data):
        register_ser = RegisterService()
        user = register_ser.createUser(validated_data)
        if user is not None:
            recipient_list = [validated_data.get('email')]
            emailService = EmailService("Registration confirmation Email",recipient_list)
            emailService.sendRegistrationEmail(validated_data.get("username"),validated_data.get('password'))
        return user


class FacultySerializer(serializers.ModelSerializer):
    faculty_user = UserAccountSerializer()
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
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
            print('user data ---> ',user_val_data.get('email'))
            recipient_list = [user_val_data.get('email')]
            emailService = EmailService("Registration confirmation Email",recipient_list)
            emailService.sendRegistrationEmail(user_val_data.get("username"),user_val_data.get('password'))
            # username = user_val_data.get('username')
            # password = user_val_data.get("password")
            # message = f"You are successfully register in ADGITM_ERP\n Username : {username} Password {password}"
            # print(message)
            # send_email_task.delay("Registration confirmation Email",message,recipient_list)

        if user is not None and faculty_result is not None:
            return user
        else:
            return None
        
class GetFacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"
        depth=1

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
