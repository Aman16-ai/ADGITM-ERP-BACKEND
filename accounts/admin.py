from django.contrib import admin
from .models import UserAccount,Faculty,Subject
# Register your models here.

# admin.site.register((UserAccount,Faculty,Subject))
@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email',"username",'first_name',"last_name", 'role','created_on']
    # list_display = [field.name for field in User._meta.get_fields()]
    search_fields = ['email']

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_user',"department"]
    search_fields = ['faculty_id']