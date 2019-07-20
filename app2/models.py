from __future__ import unicode_literals

from _json import make_encoder

from django.db import models
regno=''

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



class CrimeFill(models.Model):

    regno=models.CharField(max_length=50)
    carbrand=models.CharField(max_length=60)
    Ownername=models.CharField(max_length=60)
    Licence=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)

    @staticmethod
    def validate(regnum):
        print(regnum)
        try:
         contents=CrimeFill.objects.get(regno=regnum)
         print(contents.Email)
         return 1
        except CrimeFill.DoesNotExist:
          return 0


class Databse(models.Model):
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    otp=models.CharField(max_length=100)




    @staticmethod
    def validteuser(email,password):
        print(email,password)
        print(email,password)
        try:
         contents=Databse.objects.get(email=email,password=password)
         print(contents.email)
         return 'yes'
        except Databse.DoesNotExist:
          return 0

    @staticmethod
    def validteotp(email):

        print(email)
        try:
         contents=Databse.objects.get(email=email)
         print(contents.email)
         return contents.otp
        except Databse.DoesNotExist:
          return 0



class UpdateCrime(models.Model):

    RTO_id=models.CharField(max_length=50)
    Reg_no = models.CharField(max_length=50)
    carbrand=models.CharField(max_length=60)
    Ownername=models.CharField(max_length=60)
    Licence=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Acc_Address = models.CharField(max_length=100)
    Date = models.DateField()
    Time = models.TimeField()
    Incident=models.CharField(max_length=500)



class AllVehicle(models.Model):

    regno=models.CharField(max_length=50)
    carbrand=models.CharField(max_length=60)
    vname = models.CharField(max_length=60)
    Ownername=models.CharField(max_length=60)
    Licence=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Age = models.CharField(max_length=20)
    Temp_Address = models.CharField(max_length=20)
    Pan = models.CharField(max_length=20)
    Fuel = models.CharField(max_length=20)
    Class = models.CharField(max_length=20)
    Vehicle_is = models.CharField(max_length=20)
    Color = models.CharField(max_length=20)
    YOM = models.CharField(max_length=20)
    Engine_NO = models.CharField(max_length=20)
    Seating_Cap = models.CharField(max_length=20)

    @staticmethod
    def validate(regnum):
        print(regnum)
        try:
         contents=AllVehicle.objects.get(regno=regnum)
         print(contents.Email)
         return 1
        except AllVehicle.DoesNotExist:
          return 0

