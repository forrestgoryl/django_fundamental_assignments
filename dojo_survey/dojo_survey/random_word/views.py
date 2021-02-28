from django.shortcuts import render, redirect
import random

def random_word(request):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'v', 'w', 'x', 'y', 'z']
    word_length = random.randrange(2, 20)
    random_word = ""
    for i in range(word_length):
        # fill word based on word length
        random_word += alphabet[random.randint(1, 26)]
    if "attempt_number" in request.session:
        request.session["attempt_number"] += 1
    else:
        request.session["attempt_number"] = 0
    context = {
        "random_word": random_word,
        "attempt_number": request.session["attempt_number"]
    }
    return render(request, "random_word.html", context)