from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['f_name']) < 2:
            errors['f_name'] = "Your first name wasn't entered correctly."
        if len(postData['l_name']) < 2:
            errors['l_name'] = "Your last name wasn't entered correctly."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Your email wasn't entered correctly."
        if not re.fullmatch(r'[A-Za-z0-9!@#$%^&+=]{8,}', postData['pw']):
            errors['pw'] = "Please enter your password with at least 8 characters. Here are the accepted symbols: ! @ # $ % ^ & * ="
        if not re.search(r"[!@#$%^&*=]{1,}", postData['pw']):
            errors['pw'] = "Please use at least one of these symbols in your password: ! @ # $ % ^ & * ="
        if not re.search(r"[A-Z]{1,}", postData['pw']):
            errors['pw'] = "Please use at least one capital letter in your password."
        if not re.search(r"[0-9]{1,}", postData['pw']):
            errors['pw'] = "Please use at least one number in your password."
        if not re.search(r"[a-z]{1,}", postData['pw']):
            errors['pw'] = "Please use at least one lowercase letter in your password."
        if postData['pw'] != postData['confirm_pw']:
            errors['pw'] = "The password you entered doesn't match the password in the Confirm Password field."
        for user in User.objects.all():
            if user.email == postData['email']:
                errors['email'] = "Your email is already registered with another account. Try logging in."
        return errors
    
    def validate_login(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if len(user) > 0:
            # hashed_pw = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
            if (bcrypt.checkpw(postData['pw'].encode(), user[0].pw.encode())):
                pass
            else:
                errors['password_incorrect'] = "Your password didn't match the one in our system."
                return errors
        else:
            errors['email_not_found'] = "Your email address isn't in the system. Please register it."
        return errors

class User(models.Model):
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    pw = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()