from typing import Any
from django.core.management.base import BaseCommand
from accounts.models import UserAccount
class Command(BaseCommand):
    help = "Command to create owner account"

    def handle(self, *args: Any, **options: Any) -> str | None:
        try:
            user = UserAccount(username="Adit1234",first_name="Adit",last_name="Saxena",email="adit1234@gmail.com",role="Admin")
            user.set_password("saxena7531")
            user.save()
            print("Admin created successfully")
        except Exception as e:
            print(e)

