from django.shortcuts import render, redirect
from favorite_books_app.models import User, Book
from django.contrib import messages
import bcrypt

def landingpage(request):
    return render(request, 'landingpage.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validate_registration(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                    messages.error(request, value)
            return redirect("/")
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            request.session['first_name'] = first_name
            request.session['email'] = email
            request.session['registered'] = True
            request.session['edit'] = False
            return redirect("/homepage")
    else:
        return redirect("/")

def login(request):
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                    messages.error(request, value)
            return redirect("/")
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['first_name'] = user.first_name
            request.session['email'] = user.email
            request.session['registered'] = False
            request.session['edit'] = False
            return redirect("/homepage")
    else:
        return redirect("/")

def homepage(request):
    if 'first_name' in request.session:
        user = User.objects.get(email=request.session['email'])
        context = {
            'users': User.objects.all(),
            'books': Book.objects.all(),
            'favorites': user.liked_books.all(),
        }
        request.session['edit'] = False
        return render(request, "homepage.html", context)
    else:
        return redirect("/")

def add_book(request):
    if request.method == "POST":
        errors = Book.objects.validate_book(request.POST)
        if len(errors) > 0:
            for key, value in errors:
                messages.error(request, value)
        else:
            user = User.objects.get(email=request.session['email'])
            new_book = Book.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                uploaded_by=user,
            )
            new_book.users_who_like.add(user)
            new_book.save()
    return redirect("/homepage")

def edit_book(request):
    if request.method == 'POST':
        request.session['edit'] = True
    return redirect(f"/view_book/{request.POST['id']}")

def edit(request):
    id = request.POST['id']
    if request.method == 'POST':
        errors = Book.objects.validate_book(request.POST)
        if len(errors) > 0:
            for key, value in errors:
                messages.error(request, value)
        else:
            book = Book.objects.get(id=id)
            book.title = request.POST['title']
            book.description = request.POST['description']
            book.save()
    request.session['edit'] = False
    
    return redirect(f"/view_book/{id}")

def delete(request):
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['id'])
        book.delete()
        return redirect("/homepage")        
    else:
        return redirect(f"/view_book/{request.POST['id']}")

def book(request, id):
    if len(Book.objects.filter(id=id))> 0:
        context = {
            'book': Book.objects.get(id=id),
            'people': Book.objects.get(id=id).users_who_like.all(),
            'user': User.objects.get(email=request.session['email']),
        }
        if request.session['edit'] == True:
            context['edit'] = True
        else:
            context['edit'] = False
        return render(request, "view_book.html", context)
    else:
        messages.error(request, "The book's description page doesn't exist")
        return redirect("/homepage")

def favorite_book(request):
    if request.method == 'POST':
        book = Book.objects.get(title=request.POST['title'])
        user = User.objects.get(email=request.session['email'])
        user.liked_books.add(book)
        user.save()
        return redirect("/homepage")

def unfavorite(request):
    if request.method == 'POST':
        book = Book.objects.get(id=request.POST['id'])
        book.users_who_like.remove(User.objects.get(email=request.session['email']))
        book.save()
    return redirect(f"/view_book/{request.POST['id']}")

def logout(request):
    request.session.flush()
    return redirect("/")