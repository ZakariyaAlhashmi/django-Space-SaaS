from django.shortcuts import render
from django.core.mail import send_mail, mail_admins
from django.conf import settings

# Create your views here.

def send_massage(request):

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        Fname = request.POST['fname'] 
        Lname = request.POST['lname'] 
        Email = request.POST['email'] 
        allmessage ='From: ' + Fname +' '+ Lname + "\n \n" +"Email: "+ Email +"\n \n"+ message

        mail_admins(
            subject,
            allmessage,
            fail_silently=False
        )
    return render(request,'contact_us/contact_us.html',{})
