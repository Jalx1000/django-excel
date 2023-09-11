from django.shortcuts import render
from apps.users.models import Person

def dashboard(req):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(req, "dashboard.html", context)
