from django.shortcuts import render, redirect
from login_register_app.models import User, Message, Comment
from django.contrib import messages
import bcrypt

def login_page(request):
    return render(request, 'login_page.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_register(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else: 
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            email = request.POST['email']
            pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                f_name=f_name, 
                l_name=l_name, 
                email=email, 
                pw=pw)
            request.session['registered'] = True
            request.session['f_name'] = f_name
            return redirect("/theWall")

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            request.session['f_name'] = User.objects.get(email=request.POST['email']).f_name
            request.session['email'] = request.POST['email']
            request.session['registered'] = False
            return redirect("/theWall")

def theWall(request):
    if 'f_name' in request.session:
        context = {
            'first_name': request.session['f_name'],
            'registered': request.session['registered'],
            'messages': Message.objects.all(),
            'comments': Comment.objects.all()
        }
        return render(request, 'theWall_page.html', context)
    else:
        return redirect("/")

def post_message(request):
    if request.method == "POST":
        Message.objects.create(
            user = User.objects.get(email=request.session['email']), 
            message = request.POST['message']
        )
        return redirect("/theWall")

def post_comment(request):
    if request.method == "POST":
        print(request.POST['message_id'])
        Comment.objects.create(
            user = User.objects.get(email=request.session['email']),
            message = Message.objects.get(id=request.POST['message_id']),
            comment = request.POST['comment']
        )
        return redirect("/theWall")

def logout(request):
    request.session.flush()
    return redirect("/")