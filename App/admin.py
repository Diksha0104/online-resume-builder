from django.contrib import admin
from App.models import Form_data
from .models import profileImages

admin.site.register(profileImages)
# from App.models import user_data
# Register your models here.
# class db_admin(admin.ModelAdmin):
#     list_display=("name","email","password")

# admin.site.register(user_data,db_admin)

class db_admin(admin.ModelAdmin):
     list_display=("f_name","l_name","dob","address","phone_number","email")

admin.site.register(Form_data,db_admin)