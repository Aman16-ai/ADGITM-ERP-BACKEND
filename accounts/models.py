from django.db import models
from django.contrib.auth.models import Group, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, UserManager
from departmenant_managnement.models import Department
# Create your models here.

role_choice = [
    ("Manager","Manager"),
    ("Director","Director"),
    ("CEO","CEO"),
    ("Owner","Owner"),
    ("HOD","HOD"),
    ("DI","DI"),
    ("Professor","Professor"),
    ("Assistant Professor","Assistant Professor"),
    ("Student","Student"),
    ("MM","MM")
]

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

subject_choice = [
    ("DBMS","DBMS"),
    ("PSLA","PSLA"),
    ("CN","CN"),
    ("DS","DS"),
    ("ML","ML"),
    ("FODS","FODS"),
    ("PAI","PAI"),
    ("SE","SE"),
    ("OOPS","OOPS")
]
class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True,unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    password_changed = models.BooleanField(default=False)
    role = models.CharField(choices=role_choice, max_length=50)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        default_permissions = ('add', 'view', 'change', 'delete')




class Faculty(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    faculty_id = models.CharField(max_length=50,unique=True)
    faculty_user = models.OneToOneField(UserAccount,on_delete=models.CASCADE,related_name="user_fac")
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,blank=True)
    joined_at = models.DateField()
    salary = models.PositiveIntegerField()
    last_promotion_on = models.DateField(null=True,blank=True)
    experience = models.IntegerField()

    def __str__(self) -> str:
        return self.faculty_user.first_name + " " + self.faculty_user.last_name + " " + self.faculty_id

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE,related_name="faculty_sub")
    subject_name = models.CharField(choices=subject_choice,max_length=100),

    def __str__(self) -> str:
        return self.name
