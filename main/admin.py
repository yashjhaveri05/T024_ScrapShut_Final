from django.contrib import admin
from .models import User,NGO,Requirements,Donations
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile_number', 'address','city','pincode','is_NGO','is_Donor')}),
    )

admin.site.register(User, MyUserAdmin)
admin.site.register(NGO)
admin.site.register(Requirements)
admin.site.register(Donations)