from ..models import UserAccount,Faculty,Subject
from django.contrib.auth.models import Group
class RegisterService:


    def createUser(self,user_acc):
        user = UserAccount(**user_acc)
        user.set_password(user_acc['password'])
        user.save()
        if(user_acc['role'] in ['Manager','Owner','Director','HOD','DI','CEO']):
            group = Group.objects.get(name="Higher Authorities")
            user.groups.add(group)
        return user
    def registerFaculty(self,user_data,user):
        print(user_data)
        user_data['faculty_user'] = user
        faculty_profile = Faculty(**user_data)
        faculty_profile.save()
        return faculty_profile
