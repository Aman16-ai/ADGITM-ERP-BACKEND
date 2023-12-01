from ..models import UserAccount

class UserService:

    def getEmailsofAllMaintenaceManager(self):
        allMaintenaceManager = UserAccount.getUserBasedOnRole(role='MM')
        queryset = allMaintenaceManager.values_list('email',flat=True)
        return list(queryset)
