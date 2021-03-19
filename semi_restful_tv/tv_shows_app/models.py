from django.db import models
import re, datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        DATE_REGEX = re.compile(r"\d\d\d\d-\d\d-\d\d")
        title_list = []
        date = datetime.datetime.now()
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")
        for show in Show.objects.all():
            title_list.append(show.title)
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "The title you entered was too short. Show titles should be longer, shouldn't they?"
        if postData['title'] in title_list:
            errors['title'] = "The title you entered was the same as a show already entered before. Please select a different movie to enter."
        if len(postData['network']) < 3:
            errors['network'] = "The network name you entered was too short. No networks go by only 2 or fewer characters."
        if not DATE_REGEX.match(postData['release']):
            errors['release'] = "The release date you entered doesn't have the right format. Please enter your release date like so: YYYY-MM-DD."
        if int(postData['release'][0:4]) > int(year):
            errors['release'] = "The release date you entered is in the future."
        if int(postData['release'][0:4]) == int(year):
            if int(postData['release'][5:7]) > int(month):
                errors['release'] = "The release date you entered is in the future."
            elif int(postData['release'][5:7]) == int(month):
                if int(postData['release'][8:10]) > int(day):
                    errors['release'] = "The release date you entered is in the future."
                else:
                    pass
            else:
                pass
        if len(postData['desc']) < 10:
            errors['desc'] = "Please make your description longer."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()