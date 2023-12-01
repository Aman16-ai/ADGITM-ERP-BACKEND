from typing import Any
from django.core.management.base import BaseCommand
from accounts.models import UserAccount
class Command(BaseCommand):
    help = "Command to create owner account"

    def handle(self, *args: Any, **options: Any) -> str | None:
        try:
            user = UserAccount(username="aman7531",first_name="Aman",last_name="Saxena",email="asaxena7531@gmail.com",role="Owner")
            user.set_password("saxena7531")
            user.save()
            print("Onwer created successfully")
        except Exception as e:
            print(e)

