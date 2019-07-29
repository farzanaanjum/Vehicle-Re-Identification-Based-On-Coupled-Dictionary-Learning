# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from random import random
from .models import   RTO
from app2.models import AllVehicle
# Create your views here.
loginUser = ""
loginFlag = False
forgotEmpID = ""

def register(request):
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()

        emp_id = request.POST['emp_id']
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        branch = request.POST['branch']

        gender = request.POST['gender']
        phone = request.POST['phone']
        repeat_password = request.POST['repeat_password']
        print(emp_id, name, password, email, branch,  gender, phone, repeat_password)
        count = 0
        message = ""
        searchObject = RTO.objects.all()
        flag = 1
        for i in range(len(searchObject)):
            lst = str(searchObject[i]).split(";")
            print(lst[0], emp_id)
            if lst[0] == emp_id:
                message = message + "Employee already exists.\n"
                flag = 0
                break
        if flag == 1:
            count = count + 1

        if password == repeat_password:
            if len(password) > 6:
                flag1, flag2, flag3 = 0, 0, 0
                for i in range(len(password)):
                    ele = ord(password[i])
                    if ele > 96 and ele < 123:
                        flag1 = 1
                    elif ele > 47 and ele < 58:
                        flag2 = 1
                    elif ele > 64 and ele < 91:
                        flag3 = 1
                if flag1 == 1 and flag2 == 1 and flag3 == 1:
                    count = count + 1
                else:
                    message = message + "Re-enter the Password.\n"
        else:
            message = message + "Passwords does not match.\n"

        print(count)
        if count == 2:
            raw_text = password
            encrypt_text = raw_text
            RTO(emp_id=emp_id,
                     name=name,
                     password=encrypt_text,
                     email=email,
                     branch=branch,
                     gender=gender,
                     phone=phone).save()

            message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}
        return render(request, 'RTO/register.html', context)

    else:
        message = "Welcome To Registration Page"
        context = {"message": message}
        return render(request, 'RTO/register.html', context)


def login(request):
    global loginFlag,loginUser
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username,password)
        message = ""

        if len(RTO.objects.filter(emp_id=username)) == 0:
            message = message + "No Matching Accounts Found"
        else:
            pass_hash = str(RTO.objects.filter(emp_id=username)[0]).split(";")[4]
            decrypt_text = pass_hash
            if password == decrypt_text:
                message = message + "Welcome to the Home Page"
                loginFlag = True
                loginUser = username
                print(loginUser)
                return redirect('home')
            else:
                message = message + "Wrong Password Entered"

        print(message)
        context = {"message":message}
        return render(request,'RTO/login.html',context)

    else:
        return render(request,'RTO/login.html')


def home(request):
    global loginFlag,loginUser,loginName
    if loginFlag == False:
        return redirect('login')

    loginObj = str(RTO.objects.filter(emp_id=loginUser)[0]).split(";")
    name = loginObj[1]
    loginName = name
    print("Name:",name)

    context = {"name":name}
    return render(request,'RTO/home.html',context)




def addvehicles(request):
    if request.method == 'POST':
        print()
        print(type(request.POST))
        print()

        reg_no = request.POST['reg_no']
        carbrand = request.POST['carbrand']
        vname = request.POST['vname']
        Ownername = request.POST['Ownername']
        Licence = request.POST['Licence']
        Address = request.POST['Address']
        Email = request.POST['Email']
        Age =  request.POST['Age']
        Temp_Address =  request.POST['Temp_Address']
        Pan =  request.POST['Pan']
        Fuel =  request.POST['Fuel']
        Class = request.POST['Class']
        Vehicle_is = request.POST['Vehicle_is']
        Color = request.POST['color']
        YOM =  request.POST['YOM']
        Engine_NO = request.POST['Engine_NO']
        Seating_Cap =  request.POST['Seating_Cap']




        print(reg_no, carbrand, Ownername, Licence, Address,  Email)
        count = 0
        message = ""
        searchObject = AllVehicle.objects.all()
        flag = 1
        for i in range(len(searchObject)):
            lst = str(searchObject[i]).split(";")
            print(lst[0], reg_no)
            if lst[0] == reg_no:
                message = message + "Employee already exists.\n"
                flag = 0
                break
        if flag == 1:
            count = count + 1

            AllVehicle(regno=reg_no,
                        carbrand=carbrand,
                        vname=vname,
                        Ownername=Ownername,
                        Licence=Licence,
                        Address=Address,
                        Email=Email,Age=Age,Temp_Address=Temp_Address,Pan=Pan,
                        Fuel=Fuel,Class=Class,Vehicle_is=Vehicle_is,
                       Color=Color,YOM=YOM,Engine_NO=Engine_NO,Seating_Cap=Seating_Cap).save()

            message = message + "Account Successfully Created."
        print(message)
        context = {'message': message}
        return render(request, 'RTO/Success.html', context)

    else:
        message = "Welcome To Registration Page"
        context = {"message": message}
        return render(request, 'RTO/addvehicle.html', context)


from app2.models import UpdateCrime

def viewcrime(request):

    data=UpdateCrime.objects.all().order_by("-Date")

    context={"crime":data}
    return render(request, 'RTO/viewcrime.html',context)