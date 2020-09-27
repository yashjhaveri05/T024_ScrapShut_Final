from django.contrib import admin
from .models import User,NGO,Requirements,Donations, Gifts, Redeemed
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('mobile_number', 'address','city','pincode','is_NGO','is_Donor','credit',)}),
    )
    list_filter = ("is_NGO", "is_Donor",)

class NGOAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User", {'fields': ["user"]}),
        ("Organisation Name", {'fields': ["organisation_name"]}),
        ("Registration Number", {'fields': ["registration_no"]}),
        ("Certificate", {'fields': ["certificate"]}),
        ("Website", {'fields': ["website_link"]}),
        ("Is Verified", {'fields': ["is_verified"]}),
    ]
    list_display = ('user','organisation_name','registration_no','is_verified','website_link')
    list_filter = ("is_verified",)

class RequirementsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("created_by", {'fields': ["created_by"]}),
        ("Equipments", {'fields': ["equipments"]}),
        ("Quantity", {'fields': ["quantity"]}),
        ("Description", {'fields': ["description"]}),
        ("Reason", {'fields': ["reason"]}),
        ("Required By", {'fields': ["required_by"]}),
        ("Additional", {'fields': ["additional"]}),
    ]
    list_display = ('created_by','equipments','quantity','required_by',)

class DonationAdmin(admin.ModelAdmin):
    list_display = ('donated_by','equipment_donated','quantity_donated', 'request_made', 'donated_on', 'validated',)
    list_filter = ("validated",)

class GiftsAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Image", {'fields': ["image"]}),
        ("Name", {'fields': ["name"]}),
        ("Description", {'fields': ["description"]}),
        ("Price", {'fields': ["price"]}),
    ]
    list_display = ('name','price')

class RedeemedAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Redeemed By", {'fields': ["redeemed_by"]}),
        ("Gift", {'fields': ["gift"]}),
        ("Redeemed On", {'fields': ["redeemed_on"]}),
    ]
    list_display = ('redeemed_by','gift','redeemed_on')


admin.site.register(User, MyUserAdmin)
admin.site.register(NGO,NGOAdmin)
admin.site.register(Requirements,RequirementsAdmin)
admin.site.register(Donations,DonationAdmin)
admin.site.register(Gifts,GiftsAdmin)
admin.site.register(Redeemed,RedeemedAdmin)