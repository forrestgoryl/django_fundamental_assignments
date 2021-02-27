from django.shortcuts import render, redirect

def index(request):
    print("Displaying index view.")
    return render(request, "index.html")


def result(request):
    if request.method == "POST":
        print("A POST request was made. Displaying information.")
        context = {
            "name": request.POST["name"],
            "age": request.POST["age"],
            "gender": request.POST["gender"],
            "location": request.POST["location"].title(),
            "destinations": request.POST["destinations"],
            "comments": request.POST["comments"]
        }
        return render(request, "result.html", context)
    else:
        print("No POST request was made. Redirecting...")
        return redirect("/")
