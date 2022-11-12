from django.shortcuts import render, redirect
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import *
from PIMS import settings
from django.core.mail import send_mail ,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from . tokens import generate_token


# Create your views here.


def index(request):
    return render(request, "authentication/index.html")


def signup(request):

    if request.method == "POST":

        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Successfully created !!")


        ### EMAIL ###
        
       
        # message =  "Hello "+ myuser.first_name +"\n Welcome ..!!"
        # from_email = settings.EMAIL_HOST_USER
        # to_email =[ myuser.email]
        
        # send_mail(subject,message,from_email,to_email,fail_silently = True)        


        ##Confirmation email
        
        current_site = get_current_site(request)
        subject = "Confirmation Email ..!"
        message = render_to_string('email_confirmation.html',{
            'name':myuser.first_name,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        
        
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        
        email.fail_silently = True
        email.send()
        
        return redirect("signin")

    return render(request, "authentication/signup.html")

def activate(request,uidb64,token):
    try:
        uid =   force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk = uid)
        
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('index')
    else:
        return render(request, 'activation_failed.html')
    
def signin(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "dashboard/index.html", {'fname': firstname})
            # return render(request, "authentication/index.html", {'fname': firstname})

        else:
            messages.error(request, "Bad Credentials")
            return redirect('signin')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "logout successfully ..!")
    return redirect('signin')
