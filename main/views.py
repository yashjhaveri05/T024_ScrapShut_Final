from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User, NGO, Requirements, Donations, Gifts, Redeemed
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from .forms import Requirementsform
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from main.serializers import UserSerializer,NGOSerializer,RequirementsSerializer,DonationsSerializer
from rest_framework import mixins
from rest_framework import generics

class UserList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class NGOList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RequirementsList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class DonationsList(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Donations.objects.all()
    serializer_class = DonationsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

def ngo(request):
    if request.method == 'GET':
        return render(request, 'main/ngo_signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('add1')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        mobile_number = request.POST.get('mobile_number')
        organisation_name = request.POST.get('organisation_name')
        registration_no = request.POST.get('registration_no')
        certificate = request.POST.get('certificate')
        website_link = request.POST.get('link')
        password = request.POST.get('password')
        confirm = request.POST.get('password2')
        if password == confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('main:ngo_signup')
            else:
                user = User.objects.create(password=make_password(password), email=email, username=username, mobile_number=mobile_number,
                                                address=address,city=city,pincode=pincode,is_NGO=True)
                additional = NGO.objects.create(user=user,organisation_name=organisation_name,registration_no=registration_no,
                                                certificate=certificate,website_link=website_link)
                return redirect('main:ngo_signup')
        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('main:ngo_signup')

def donor_signup(request):
    if request.method == 'GET':
        return render(request, 'main/donor_signup.html')

    elif request.method == 'POST':
        first_name = request.POST.get('username')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('add1')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        confirm = request.POST.get('password2')
        if password == confirm:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('main:donor_signup')
            else:
                user = User.objects.create(first_name=first_name,last_name=last_name,password=make_password(password), email=email, username=username, mobile_number=mobile_number,
                                                address=address,city=city,pincode=pincode,is_Donor=True)
                login(request, user)
                return redirect('main:home')
        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('main:donor_signup')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'main/login_view.html')
    
    elif request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request, user)
            return redirect('main:home')
        else:
            messages.info(request, 'Invalid Credentials !')
            return redirect('main:login_view')

def logout(request):
    auth.logout(request)
    return render(request,'main/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        form = Requirementsform(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.created_by = request.user
            temp.save()
        return redirect('main:home')

    else:
        form = Requirementsform()
        return render(request,'main/requirement_create.html',{'form':form})

def ngo_req(request):
    requirements = Requirements.objects.filter(created_by=request.user)
    context = {
        'requirements':requirements
    }
    return render(request, 'main/display_requirements.html', context)

def update(request,requirement_id):
    instance = Requirements.objects.get(id=requirement_id)
    if request.method == 'POST':
        form = Requirementsform(request.POST,instance=instance)
        if form.is_valid():
            form.save()
        return redirect('main:home')

    else:
        instance = Requirements.objects.get(id=requirement_id)
        form = Requirementsform(instance=instance)
        return render(request,'main/update.html',{'form':form})

def delete(request,requirement_id):
    Requirements.objects.filter(id=requirement_id).delete()
    return redirect('main:home')

def home(request):
    requirements = Requirements.objects.all()
    context = {
        'requirements':requirements
    }
    return render(request, 'main/homepage.html', context)

def requirements_detail(request,pk):
    requirements = Requirements.objects.filter(id=pk)
    context = {
        'requirements':requirements
    }
    return render(request, 'main/detail.html', context)

def donate(request):
    if request.method == "POST":
        donated_by = request.user
        pk = request.POST.get("pk")
        requirement = Requirements.objects.get(id=pk)
        quantity_donated = request.POST.get("quantity_donated")
        donation = Donations(donated_by=donated_by, equipment_donated=requirement, quantity_donated=quantity_donated)
        donation.save()
        messages.success(request, "Thankyou for donating!!")
    return redirect("home")

def donations_made(request):
    donations = Donations.objects.filter(donated_by=request.user)
    context = {
        'donations' : donations
    }
    return render(request, 'main/donations_made.html', context)

def donations_received(request):
    donations = Donations.objects.filter(equipment_donated__created_by=request.user)
    context = {
        'donations' : donations
    }
    return render(request, 'main/donations_received.html', context)

def validate(request,pk):
    donations = Donations.objects.filter(id=pk)
    donor = donations[0]
    donated_on = timezone.now()
    donations.update(validated=True, donated_on=donated_on)
    users = User.objects.filter(username=donor)
    for user in users:
        if user.is_Donor:
            user.credit = user.credit + 20
    credit = user.credit
    users.update(credit=credit)
    return redirect('main:home')

def gifts(request):
    gifts = Gifts.objects.all()
    context = {
        'gifts' : gifts,
    }
    return render(request, 'main/gifts.html', context)

def redeem(request,pk):
    gifts = Gifts.objects.filter(id=pk)
    for gift in gifts:
        price = int(gift.price)
    redeemed = Redeemed(redeemed_by=request.user,gift=gift)
    redeemed.save()
    users = User.objects.filter(username=request.user)
    for user in users:
        credit = user.credit
    if price>credit:
        messages.success(request, "Insufficient Credits!!Earn more by donating more!!")
    else:
        credit = credit-price
        messages.success(request, "You will get your gift in 10 days!!")
    users.update(credit=credit)
    return redirect("main:home")

def redeemed_gifts(request):
    redeemed_gifts = Redeemed.objects.filter(redeemed_by=request.user)
    context = {
        'redeemed_gifts' : redeemed_gifts
    }
    return render(request, 'main/redeemed_gifts.html', context)

def router(request):
    return render(request, 'main/signup_options.html')