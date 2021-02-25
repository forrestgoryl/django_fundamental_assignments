from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    from django.shortcuts import render
    return render(request, 'index.html', context)
