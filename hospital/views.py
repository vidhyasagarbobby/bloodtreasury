from django.shortcuts import render, redirect
from hospital.models import Hospital
from donor.models import Donor
from bloodbank.models import BloodBank
from django.contrib import messages
from django.db import connection
import psycopg2

# Create your views here.
def hospital(request):
    return render(request, 'hospital.html')

def login(request):
    if request.method=='POST':
        user = Hospital.objects.get(id=2)
        password = request.POST.get('password')
        if user.password == password:
            user.is_authenticated = True
            user.save()
            return redirect('./dashboard')
        else:
            messages.error(request, 'Wrong Password')
            return redirect('/hospital')
def logout(request):
    user = Hospital.objects.get(id=2)
    user.is_authenticated = False
    user.save()
    return redirect('./')

def dashboard(request):
    user = Hospital.objects.get(id=2)
    data={}
    data['hospital'] = user
    return render(request, 'Hdashboard.html', data)

def findblood(request):
    hospital = Hospital.objects.get(id=2)
    blood_group = request.POST.get('blood_group')
    donors = Donor.objects.filter(blood_group=blood_group).order_by('-dod')
    blooddic = {"A+":"a_pos", "A-":"a_neg", "B+":"b_pos", "B-":"b_neg", "O+":"o_pos", "O-":"o_neg", "AB+":"ab_pos", "Ab-":"ab_neg"}
    blood = blooddic[blood_group]
    sql="select bb.id, bb.name, bs."+blood+", bb.phone, bb.email, bb.address, bb.website from public.bloodbank_bloodbank as bb, public.bloodbank_bloodstock as bs where bs."+blood+">0 and bb.id=bs.bloodbank_id order by bs."+blood+" desc;"
    cursor = connection.cursor()
    cursor.execute(sql)
    bloodbanks = cursor.fetchall()
    for i in bloodbanks:
        print(i[1])
    data={}
    data['hospital'] = hospital
    data['donors'] = donors
    data['bloodbanks'] = bloodbanks

    return render(request, 'findBlood.html', data)