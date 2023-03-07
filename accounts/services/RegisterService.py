from ..models import UserAccount,Faculty,Subject
class RegisterService:


    def createUser(self,user_acc):
        # user = UserAccount.objects.create_user(username=self.user_acc['username'],
        #                                 email=self.user_acc['email'],
        #                                 password=self.user_acc['password'])
        # user.first_name = self.user_acc['first_name']
        # user.last_name = self.user_acc['last_name']
        user = UserAccount(**user_acc)
        user.set_password(user_acc['password'])
        user.save()
        return user
    def registerFaculty(self,user_data,user):
        print(user_data)
        user_data['faculty_user'] = user
        faculty_profile = Faculty(**user_data)
        faculty_profile.save()
        return faculty_profile
