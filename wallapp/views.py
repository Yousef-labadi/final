from django.shortcuts import render,redirect
from wallapp.models import *
from django.contrib import messages
import bcrypt 
def form(request):
    return render(request,'form.html')
def reg(request):
    errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else :
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pwd']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        password=pw_hash
        User.objects.create(fname=fname,lname=lname,email=email,password=pw_hash)
        newUser=User.objects.last().fname
        request.session['newUser']=newUser
        request.session['fname'] = fname
        
        return redirect('/success')
def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['pwd'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['fname'] = logged_user.fname
            
            # never render on a post, always redirect!
            return redirect('/success')
            
    return redirect("/")
def success(request):
    return render(request,'success.html')
def wall(request):
    pass
    return render(request,'wall.html')
def addmessage(request):
    m=request.POST['message']
    Message.objects.create(message=request.POST['message'])
    
    return redirect('/add-message',)

def destroy(request):
    request.session.clear()
    return redirect('/')