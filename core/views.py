# from django.shortcuts import render

# def error_404_view(request):
#     return render(request, '404.html', status=404)

from django.shortcuts import render

def index(req):
    return render(req, "index.html")
