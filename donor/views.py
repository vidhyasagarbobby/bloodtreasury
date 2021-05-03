from django.shortcuts import render, redirect
from django.contrib import messages
from donor.models import Donor, DonationHistory
import psycopg2

# Create your views here.
def donor(request):
    return render(request, 'donor.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        blood_group = request.POST.get('blood_group')
        dod = request.POST.get('dod')
        state = request.POST.get('state')
        city = request.POST.get('city')
        if Donor.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Try with a different username.")
            return redirect('./register')
        elif Donor.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Try with a different Email.")
            return redirect('./register')
        elif Donor.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number already exists. Try with a different phone number.")
            return redirect('./register')
        elif password != confirm_password:
            messages.error(request, "Passwords did not match. Please check again.")
            return redirect('./register')
        else:
            donor = Donor.objects.create(name=name, username=username, phone=phone, email=email, password=password, dob=dob, gender=gender, blood_group=blood_group, dod=dod, state=state, city=city)
            donor.save()
            messages.success(request, "Registration successful!")
            return redirect('./login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Donor.objects.get(email=email)
        if user.password == password:
            user.is_authenticated = True
            user.save()
            return redirect(user)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('./login')
    else:
        return render(request, 'login.html')

def dashboard(request, username):
    user = Donor.objects.get(username=username)
    donationHistory = DonationHistory.objects.filter(donor_id=user.id).order_by('-dod')
    data={}
    data['donor'] = user
    data['donationHistory'] = donationHistory
    return render(request, 'dashboard.html', data)

def logout(request, username):
    user = Donor.objects.get(username=username)
    user.is_authenticated = False
    user.save()
    return redirect('../login')

def updateHistory(request, username):
    user = Donor.objects.get(username=username)
    if request.method == 'POST':
        dod = request.POST.get('dod')
        units = request.POST.get('units')
        purpose = request.POST.get('purpose')
        record = DonationHistory.objects.create(donor_id=user.id, dod=dod, units=units, purpose=purpose)
        record.save()
        user.dod = dod
        user.save()
        return redirect('./')
    else:
        data={}
        data['donor'] = user
        return render(request, 'updatehistory.html', data)

def editDetails(request, username):
    user = Donor.objects.get(username=username)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        username = request.POST.get('username')
        new_phone = request.POST.get('phone')
        new_email = request.POST.get('email')
        new_dob = request.POST.get('dob')
        new_gender = request.POST.get('gender')
        new_blood_group = request.POST.get('blood_group')
        new_dod = request.POST.get('dod')
        new_state = request.POST.get('state')
        new_city = request.POST.get('city')
        
        user.name = new_name
        user.phone = new_phone
        user.email = new_email
        user.dob = new_dob
        user.gender = new_gender
        user.blood_group = new_blood_group
        user.dod = new_dod
        user.state = new_state
        user.city = new_city
        user.save()
        return redirect('./')
    else:
        data={}
        data['donor'] = user
        return render(request, 'editdetails.html', data)

def changePassword(request, username):
    user = Donor.objects.get(username=username)
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if old_password == user.password:
            if new_password == confirm_password:
                user.password = new_password
                user.save()
                return redirect('./')
            else:
                messages.error(request, "Passwords didn't match.")
                return redirect('./change-password')
        else:
            messages.error(request, "Incorrect Password.")
            return redirect('./change-password')
    else:
        data={}
        data['donor'] = user
        return render(request, 'changepassword.html', data)