from django.shortcuts import render, redirect
from .models import User
import datetime
# import MySQLdb

def index(request):
    context = {
        'all_the_users': User.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
#     db=MySQLdb.connect(host='localhost', user='root', passwd='root', db='mydb')
#     db.query(f"""INSERT INTO mydb.users (first_name, last_name, email_address, age, created_at, updated_at)
# VALUES ({request.POST['first_name']}, {request.POST['last_name']}, {request.POST['email_address']}, {request.POST['age']}, {datetime.datetime.now()}, {datetime.datetime.now()}""")
#     db.commit()
    User.objects.create(
        first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        email_address=request.POST['email_address'], 
        age=request.POST['age'], 
        created_at=datetime.datetime.now(), 
        updated_at=datetime.datetime.now()
        )
    return redirect("/")