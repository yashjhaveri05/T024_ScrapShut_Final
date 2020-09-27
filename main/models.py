from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone

class User(AbstractUser):
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    city =  models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    is_NGO = models.BooleanField(default=False)
    is_Donor = models.BooleanField(default=False)
    credit = models.IntegerField(default=0)

class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation_name = models.CharField(max_length=25,blank=False)
    registration_no = models.CharField(max_length=30,blank=False)
    certificate = models.ImageField(default='default.png',upload_to='ngo_certificate/')
    website_link = models.URLField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.registration_no

class Requirements(models.Model):
    EQUIPMENTS = (
        ('Thermometer', 'Thermometer'),
        ('Oximeter', 'Oximeter'),
        ('KN95 Mask', 'KN95 Mask'),
        ('PPE Kit', 'PPE Kit'),
        ('3M Mask', '3M Mask'),
        ('Protective Goggles', 'Protective Goggles'),
        ('Hand Sanitizer', 'Hand Sanitizer'),
        ('Gloves', 'Gloves'),
        ('Face Shield', 'Face Shield'),
        ('Test Kit', 'Test Kit'),
        ('Ventilators', 'Ventilators'),
        ('Beds', 'Beds'),
        ('Medicines', 'Medicines'),
        ('Others', 'Others'),
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    equipments = models.CharField(max_length=32,choices=EQUIPMENTS, blank=False)
    quantity = models.IntegerField(default=1, blank=False)
    description = models.TextField(blank=True)
    reason = models.CharField(max_length=255,blank=False)
    required_by = models.DateTimeField(default=timezone.now)
    additional = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.equipments

class Donations(models.Model):
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment_donated = models.ForeignKey(Requirements, on_delete=models.CASCADE)
    quantity_donated = models.IntegerField(default=1)
    request_made = models.DateField(default=timezone.now)
    donated_on = models.DateField(default=timezone.now)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.donated_by)

class Gifts(models.Model):
    image = models.ImageField(default='default.png', upload_to='images/')
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250,blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Redeemed(models.Model):
    redeemed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gifts, on_delete=models.CASCADE)
    redeemed_on = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.redeemed_by)