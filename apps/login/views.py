from django.shortcuts import render


def login(req):
    context = {}
    return render(req, "login.html", context)
