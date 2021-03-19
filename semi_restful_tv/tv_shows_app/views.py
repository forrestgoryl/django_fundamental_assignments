from django.shortcuts import render, redirect, HttpResponse
from tv_shows_app.models import Show
from django.contrib import messages
import re

def shows(request):
    object_list = Show.objects.all()
    context = {'object_list': object_list}
    return render(request, 'shows.html', context)

def shows_id(request, show_number):
    show = Show.objects.get(id=show_number)
    context = {
        "show_number": show_number,
        "title": show.title,
        "network": show.network,
        "release": show.release,
        "desc": show.desc,
        "updated_at": show.updated_at
    }
    return render(request, 'shows_id.html', context)

def shows_new(request):
    return render(request, 'shows_new.html')

def shows_edit(request, show_number):
    context = {
        'show_number': show_number
    }
    return render(request, 'shows_edit.html', context)

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
        _title = request.POST['title']
        _network = request.POST['network']
        _release = request.POST['release']
        _desc = request.POST['desc']
        Show.objects.create(title=_title, network=_network, release=_release, desc=_desc)
        return redirect("/shows")

def update(request, show_number):
    errors = Show.objects.basic_validator(request.POST)
    if 'title' in errors.keys():
        if errors['title'] == "The title you entered was the same as a show already entered before. Please select a different movie to enter.":
            if len(errors) == 1:
                errors = {}
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/{show_number}/edit")
    else:
        show = Show.objects.get(id=show_number)
        if 'title' in request.POST != '':
            show.title = request.POST['title']
        if 'network' in request.POST != '':
            show.network = request.POST['network']
        if 'release' in request.POST != '':
            show.release = request.POST['release']
        if 'desc' in request.POST != '':
            show.desc = request.POST['desc']
        show.save()
        return redirect("/shows")

def delete(request, show_number):
    show = Show.objects.get(id=show_number)
    show.delete()
    return redirect("/shows")