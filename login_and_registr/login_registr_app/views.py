from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_register(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/homepage")
        else: 
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            email = request.POST['email']
            pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(f_name=f_name, l_name=l_name, email=email, pw=pw)
            request.session['registered'] = True
            request.session['f_name'] = f_name
            return redirect("/success")

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/homepage")
        else:
            user = User.objects.filter(email=request.POST['email'])[0].f_name
            request.session['f_name'] = user
            request.session['registered'] = False
            return redirect("/success")

def success(request):
    context = {
        'first_name': request.session['f_name'],
        'registered': request.session['registered']
    }
    return render(request, 'success.html', context)

def logout(request):
    request.session.flush()
    return redirect("/")