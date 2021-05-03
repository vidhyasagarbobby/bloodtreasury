from django.shortcuts import render, redirect
from bloodbank.models import BloodBank, BloodStock
from django.contrib import messages
import psycopg2

# Create your views here.
def bloodbank(request):
    return render(request, 'bloodbank.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        website = request.POST.get('website')
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        if BloodBank.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number already exists. Try with a different phone number.")
            return redirect('./register')
        elif BloodBank.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Try with a different Email.")
            return redirect('./register')
        elif password != confirm_password:
            messages.error(request, "Passwords did not match. Please check again.")
            return redirect('./register')
        else:
            bloodbank = BloodBank.objects.create(name=name, phone=phone, email=email, password=password, website=website, address=address, state=state, city=city)
            bloodbank.save()
            bloodstock = BloodStock.objects.create(a_pos=0, a_neg=0, b_pos=0, b_neg=0, o_pos=0, o_neg=0, ab_pos=0, ab_neg=0, bloodbank_id=bloodbank.id)
            bloodstock.save()
            messages.success(request, "Registration successful!")
            return redirect('./login')
    else:
        return render(request, 'BBregister.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = BloodBank.objects.get(email=email)
        if user.password == password:
            user.is_authenticated = True
            user.save()
            return redirect(user)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('./login')
    else:
        return render(request, 'BBlogin.html')

def logout(request, id):
    user = BloodBank.objects.get(id=id)
    user.is_authenticated = False
    user.save()
    return redirect('../login')

def dashboard(request, id):
    user = BloodBank.objects.get(id=id)
    record = BloodStock.objects.get(bloodbank_id=user.id)
    data={}
    data['bloodbank'] = user
    data['bloodstock'] = record
    return render(request, 'BBdashboard.html', data)

def updateStock(request, id):
    user = BloodBank.objects.get(id=id)
    record = BloodStock.objects.get(bloodbank_id=id) 
    if request.method == 'POST':
        a_pos = request.POST.get('a_pos')
        a_neg = request.POST.get('a_neg')
        b_pos = request.POST.get('b_pos')
        b_neg = request.POST.get('b_neg')
        o_pos = request.POST.get('o_pos')
        o_neg = request.POST.get('o_neg')
        ab_pos = request.POST.get('ab_pos')
        ab_neg = request.POST.get('ab_neg')

        record.a_pos = a_pos
        record.a_neg = a_neg
        record.b_pos = b_pos
        record.b_neg = b_neg
        record.o_pos = o_pos
        record.o_neg = o_neg
        record.ab_pos = ab_pos
        record.ab_neg = ab_neg
        record.save()
        return redirect('./')
    else:
        data={}
        data['bloodbank'] = user
        data['bloodstock'] = record
        return render(request, 'BBupdatestock.html', data)

def editDetails(request, id):
    user = BloodBank.objects.get(id=id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_phone = request.POST.get('phone')
        new_email = request.POST.get('email')
        new_website = request.POST.get('website')
        new_address = request.POST.get('address')
        new_state = request.POST.get('state')
        new_city = request.POST.get('city')
        
        user.name = new_name
        user.phone = new_phone
        user.email = new_email
        user.website = new_website
        user.address = new_address
        user.state = new_state
        user.city = new_city
        user.save()
        return redirect('./')
    else:
        data={}
        data['bloodbank'] = user
        return render(request, 'BBeditdetails.html', data)

def changePassword(request, id):
    user = BloodBank.objects.get(id=id)
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
        data['bloodbank'] = user
        return render(request, 'BBchangepassword.html', data)