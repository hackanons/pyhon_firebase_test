from django.shortcuts import render
import pyrebase

config = {

'apiKey': "AIzaSyB0Il0NLQPxxDyMgoE0fOMd4pYUkbkZVvI",
    'authDomain': "cpanel-5e873.firebaseapp.com",
    'databaseURL': "https://cpanel-5e873.firebaseio.com",
    'projectId': "cpanel-5e873",
    'storageBucket': "cpanel-5e873.appspot.com",
    'messagingSenderId': "579985583952"
  }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def singIn(request):

    return render(request, "signIn.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
    print(user)
    return render(request, "welcome.html",{"e":email})
