from django.shortcuts import render, redirect

def index(request):
    print("Displaying index view.")
    return render(request, "index.html")

# x helps identify the key in request.session that will be linked
# to user info
x = 0
def result(request):
    if request.method == "POST":
        print("-"*220)
        print("A POST request was made. Displaying information.")
        global x
        x += 1
        try:
            request.session[f"user{x}"] = {
                "name": request.POST["name"],
                "age": request.POST["age"],
                "gender": request.POST["gender"],
                "location": request.POST["location"].title(),
                "destinations": request.POST["destinations"],
                "comments": request.POST["comments"]
            }
        except KeyError:
            request.session[f"user{x}"] = {
                "name": request.POST["name"],
                "age": request.POST["age"],
                "gender": request.POST["gender"],
                "location": request.POST["location"].title(),
                "comments": request.POST["comments"]
            }
        # context = {}
        # for key in request.session.keys():
        #     print(key)
        #     context.update({key: request.session[key]})
        #     print(context[key])
        return render(request, "result.html")
    else:
        print("No POST request was made. Redirecting...")
        return redirect("/")

def wipe(request):
    request.session.flush()
    return redirect("/")
