from django.db import models
department_choice = [
    ("AIML","AIML"),
    ("AIDS","AIDS"),
    ("CSE","CSE"),
    ("IT","IT"),
    ("ECE","ECE"),
    ("EEE","EEE"),
    ("ME","ME"),
    ("MAE","MAE"),
    ("CIVIL","CIVIL"),
    ("BA-LLB","BA-LLB"),
    ("BBA","BBA"),
    ("MBA","MBA")
]

# Create your models here.
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name