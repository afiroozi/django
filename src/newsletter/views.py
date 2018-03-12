from django.shortcuts import render


# Create your views here.
# sample of view

def home(request):
    return render(request, "home.html", {})
