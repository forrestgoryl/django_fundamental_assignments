from django.shortcuts import render, redirect
from random import randint

def index(request):
    return render(request, 'index.html')

def farm(request):
    x = randint(10,20)
    if 'gold_count' not in request.session.keys():
        request.session['gold_count'] = x
        request.session['activity_log'] = f"Entered farm and earned {x}.    "
    else:
        request.session['gold_count'] += x
        request.session['activity_log'] += f"Entered farm and earned {x}.   "
    context = {
        'gold_count': request.session['gold_count'],
        'activity_log': request.session['activity_log']
    }
    return render(request, "index.html", context)

def cave(request):
    x = randint(5,10)
    if 'gold_count' not in request.session.keys():
        request.session['gold_count'] = x
        request.session['activity_log'] = f"Entered cave and earned {x}.    "
    else:
        request.session['gold_count'] += x
        request.session['activity_log'] += f"Entered cave and earned {x}.   "
    context = {
        'gold_count': request.session['gold_count'],
        'activity_log': request.session['activity_log']
    }
    return render(request, "index.html", context)

def house(request):
    x = randint(2,5)
    if 'gold_count' not in request.session.keys():
        request.session['gold_count'] = x
        request.session['activity_log'] = f"Entered house and earned {x}.   "
    else:
        request.session['gold_count'] += x
        request.session['activity_log'] += f"Entered house and earned {x}.  "
    context = {
        'gold_count': request.session['gold_count'],
        'activity_log': request.session['activity_log']
    }
    return render(request, "index.html", context)

def casino(request):
    x = randint(-50,50)
    win_lose = None
    if x >= 0:
        win_lose = "won"
    else:
        win_lose = "lost"
    if 'gold_count' not in request.session.keys():
        request.session['gold_count'] = x
        request.session['activity_log'] = f"Entered casino and {win_lose} ${x}.     "
    else:
        request.session['gold_count'] += x
        request.session['activity_log'] += f"Entered casino and {win_lose} ${x}.    "
    context = {
        'gold_count': request.session['gold_count'],
        'activity_log': request.session['activity_log']
    }
    return render(request, 'index.html', context)

def wipe(request):
    request.session.flush()
    return redirect("/")