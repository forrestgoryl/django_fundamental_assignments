from django.db import models
import bcrypt, re

class UserManager(models.Manager):
    def validate_registration(self, postData):
        first_name = postData['first_name']
        last_name = postData['last_name']
        email = postData['email']
        password = postData['password']
        confirm_password = postData['confirm_password']
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(first_name) > 20:
            errors['name'] = "Your first name is longer than 20 characters. Can you shorten it?"
        if len(last_name) > 20:
            errors['name'] = "Your last name is longer than 20 characters. Can you shorten it?"
        if not EMAIL_REGEX.match(email):
            errors['email'] = "Your email doesn't fit the pattern 'your_email@abc.com'."
        if User.objects.filter(email=email).exists():
            errors['email'] = "Your email is already registered with another account. Try logging in."
        if len(email) > 30:
            errors['email'] = "Your email is too long for the database. Use one with less than 30 characters."
        if len(password) > 255:
            errors['password'] = "Your password is too long. How can you remember that?"
        if password != confirm_password:
            errors['password'] = "Your password doesn't match your password confirmation."
        return errors
    def validate_login(self, postData):
        errors = {}
        list_user = User.objects.filter(email=postData['email'])
        if len(list_user) > 0:
            if (bcrypt.checkpw(postData['password'].encode(), list_user[0].password.encode())):
                pass
            else:
                errors['password_incorrect'] = "Your password didn't match the one in our system."
                return errors
        else:
            errors['email_not_found'] = "Your email address isn't in the system. Please register it."
        return errors

class User(models.Model):
    # uploaded_books = get a list of books uploaded by user
    # liked_books = get a list of books liked by user
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def validate_book(self, postData):
        errors = {}
        list_book = Book.objects.filter(title=postData['title'])
        if len(list_book) > 0:
            errors['book_already_added'] = "This book has already been added."
            return errors
        if len(postData['title']) < 3:
            errors['title'] = "Please make the title longer than 2 characters."
        if len(postData['description']) < 10:
            errors['description'] = "Please add a longer description."
        return errors

class Book(models.Model):
    uploaded_by = models.ForeignKey(User, related_name="uploaded_books", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
