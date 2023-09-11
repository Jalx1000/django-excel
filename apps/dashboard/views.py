from django.shortcuts import render

def dashboard(req):
    # persons = Person.objects.all()
    context = {}
    return render(req, "dashboard.html", context)
