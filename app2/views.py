from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from models import AllVehicle
from .models import Document
from .forms import DocumentForm
import DetectChars
import smtplib
import cv2
import numpy as np
import os
SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)
uploaded_file_url='dr'
showSteps = True
from . import DetectPlates
from . import DetectChars
from forms import Reg
from models import Databse
from forms import Login
from models import  UpdateCrime


def begin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print("email is", email)
        print("pass is", password)
        request.session['usermail']=email
        d = Databse()
        userdetails = d.validteuser(email=email,password=password)
        #print(userdetails.Email)
        print(userdetails)
        if userdetails =='yes':
            import random
            otp=random.randint(1,1000)

            print(otp)
            otp_update = Databse.objects.filter(email=email)[0]
            otp_update.otp = otp
            otp_update.save()
            FROM = "internsangular@gmail.com"
            TO = email if isinstance(email, list) else [email]
            SUBJECT = "Dear User otp for your Login Cred ."
            TEXT =otp

            # Prepare actual message
            message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                  """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("internsangular@gmail.com", "internship")
                server.sendmail(FROM, TO, message)
                server.close()
                print 'successfully sent the mail'
            except:
                print "failed to send mail"

            print('Successfull Login')
            return render(request, 'app2/otp.html')
        else:
            print('Failure Login')
            return render(request, 'app2/begin.html')
    form2 = Login()
    context = {'form2': form2}
    return render(request, 'app2/begin.html', context)


def otp(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        email=request.session['usermail']
        print("email is", email)

        d = Databse()
        otpdb = d.validteotp(email)
        #print(userdetails.Email)
        print(otpdb)
        if otp==otpdb:
            print('Successfull Login')
            return render(request, 'app2/index.html')
        return render(request, 'app2/otp.html')




    return render(request, 'app2/otp.html')



def signup(request):
    if request.method=='POST':
        regform=Reg(request.POST)
        if regform.is_valid():
            new_data=Databse(username=request.POST['username'],password=request.POST['password'],
                             email=request.POST['email'],address=request.POST['address'],
                             department=request.POST['department'])
            new_data.save()
            return redirect('begin')
    else:
     form1=Reg()
     context={'form1':form1}
     return render(request,'app2/register.html',context)


def index(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print (uploaded_file_url)
        blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()  # attempt KNN training
        if blnKNNTrainingSuccessful == False:  # if KNN training was not successful
            print("\nerror: KNN traning was not successful\n")  # show error message
            return  # and exit program
        # end if

        imgOriginalScene = cv2.imread(uploaded_file_url)  # open image

        if imgOriginalScene is None:  # if image was not read successfully
            print("\nerror: image not read from file \n\n")  # print error message to std out
            os.system("pause")  # pause so user can see error message
            return  # and exit program
        # end if

        listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)  # detect plates

        listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)  # detect chars in plates

        cv2.imshow("imgOriginalScene", imgOriginalScene)  # show scene image

        if len(listOfPossiblePlates) == 0:  # if no plates were found
            print("\nno license plates were detected\n")  # inform user no plates were found
        else:  # else
            # if we get in here list of possible plates has at leat one plate

            # sort the list of possible plates in DESCENDING order (most number of chars to least number of chars)
            listOfPossiblePlates.sort(key=lambda possiblePlate: len(possiblePlate.strChars), reverse=True)

            # suppose the plate with the most recognized chars (the first plate in sorted by string length descending order) is the actual plate
            licPlate = listOfPossiblePlates[0]

            cv2.imshow("imgPlate", licPlate.imgPlate)  # show crop of plate and threshold of plate
            cv2.imshow("imgThresh", licPlate.imgThresh)

            if len(licPlate.strChars) == 0:  # if no chars were found in the plate
                print("\nno characters were detected\n\n")  # show message
                return  # and exit program
            # end if

            drawRedRectangleAroundPlate(imgOriginalScene, licPlate)  # draw red rectangle around plate

            print(
                    "\nlicense plate read from image = " + licPlate.strChars + "\n")  # write license plate text to std out
            print("----------------------------------------")
            output=licPlate.strChars
            print '-----passing data',output

            upadateCrime
            vehicledetails =AllVehicle .objects.get(regno=output)
            print(AllVehicle.Email)
            cv2.waitKey(0)
            context={'vehicledetails':vehicledetails}
        #  # hold windows open until user presses a key

        return render(request, 'app2/show.html',context)




        ###################################################################################################
    return render(request, 'app2/index.html')





def upadateCrime(request):
    if request.method=='POST':
        rtoid=request.POST['id']
        regno = request.POST['regno']
        carbrand = request.POST['carbrand']
        owner = request.POST['owner']
        licence = request.POST['licence']
        address = request.POST['address']
        email = request.POST['email']
        a_address = request.POST['a_address']
        date = request.POST['date']
        time = request.POST['time']
        incident = request.POST['incident']
        print(rtoid)
        UpdateCrime(RTO_id=rtoid,Reg_no=regno,carbrand=carbrand,Ownername=owner,Licence=licence,Address=address,
                    Email=email,Acc_Address=a_address,Date=date,Time=time,Incident=incident).save()
        crime_count= UpdateCrime.objects.count()
        print("DDd",crime_count)
        total_Vehicle=AllVehicle.objects.count()
        vibe= AllVehicle.objects.get(regno=regno)
        from .models import  Databse
        totalusers=Databse.objects.count()

        request.session['email']=email

        return render(request, 'app2/preview.html',{'rtoid':rtoid,'regno':regno,'carbrand':carbrand,'owner':owner,
                                                   'licence':licence,'address':address,'email':email,'a_address':a_address,
                                                   'date':date,'time':time, 'incident':incident ,'crime_count':crime_count,
                                                    'total_Vehicle':total_Vehicle,'totalusers':totalusers,
                                                    'fueltype':vibe.Fuel,'pan':vibe.Pan,'color':vibe.Color})




    return render(request, 'app2/show.html')





def email(request):
   email=request.session['email']
   print email
   import smtplib

   FROM = "internsangular@gmail.com"
   TO = email if isinstance(email, list) else [email]
   SUBJECT = "Alert from Crime Department."
   TEXT = "Dear user your vehicle has crossed Traffic Signs"

   # Prepare actual message
   message = """From: %s\nTo: %s\nSubject: %s\n\n%s
      """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
   try:

       server = smtplib.SMTP("smtp.gmail.com", 587)
       server.ehlo()
       server.starttls()
       server.login("internsangular@gmail.com", "internship")
       server.sendmail(FROM, TO, message)
       server.close()
       print 'successfully sent the mail'
   except:
       print "failed to send mail"

   return render(request,'app2/final.html')


















def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):
    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)  # get 4 vertices of rotated rect

    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)  # draw 4 red lines
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)

    # end function

    ###################################################################################################


def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
    ptCenterOfTextAreaX = 0  # this will be the center of the area the text will be written to
    ptCenterOfTextAreaY = 0

    ptLowerLeftTextOriginX = 0  # this will be the bottom left of the area that the text will be written to
    ptLowerLeftTextOriginY = 0

    sceneHeight, sceneWidth, sceneNumChannels = imgOriginalScene.shape
    plateHeight, plateWidth, plateNumChannels = licPlate.imgPlate.shape

    intFontFace = cv2.FONT_HERSHEY_SIMPLEX  # choose a plain jane font
    fltFontScale = float(plateHeight) / 30.0  # base font scale on height of plate area
    intFontThickness = int(round(fltFontScale * 1.5))  # base font thickness on font scale

    textSize, baseline = cv2.getTextSize(licPlate.strChars, intFontFace, fltFontScale,
                                         intFontThickness)  # call getTextSize

    # unpack roatated rect into center point, width and height, and angle
    ((intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight),
     fltCorrectionAngleInDeg) = licPlate.rrLocationOfPlateInScene

    intPlateCenterX = int(intPlateCenterX)  # make sure center is an integer
    intPlateCenterY = int(intPlateCenterY)

    ptCenterOfTextAreaX = int(intPlateCenterX)  # the horizontal location of the text area is the same as the plate

    if intPlateCenterY < (sceneHeight * 0.75):  # if the license plate is in the upper 3/4 of the image
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) + int(
            round(plateHeight * 1.6))  # write the chars in below the plate
    else:  # else if the license plate is in the lower 1/4 of the image
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) - int(
            round(plateHeight * 1.6))  # write the chars in above the plate
    # end if

    textSizeWidth, textSizeHeight = textSize  # unpack text size width and height

    ptLowerLeftTextOriginX = int(
        ptCenterOfTextAreaX - (textSizeWidth / 2))  # calculate the lower left origin of the text area
    ptLowerLeftTextOriginY = int(
        ptCenterOfTextAreaY + (textSizeHeight / 2))  # based on the text area center, width, and height

    # write the text on the image
    cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY), intFontFace,
                fltFontScale, SCALAR_YELLOW, intFontThickness)






