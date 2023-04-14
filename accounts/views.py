from django.shortcuts import render


def register(request):
    return render(request, "accounts/register.html")

def profile(request):
    return render(request, "accounts/profile.html")

def login(request):
    return render(request, "accounts/login.html")

def joinCommunity(request):
    return render(request, "accounts/joincommunity.html")