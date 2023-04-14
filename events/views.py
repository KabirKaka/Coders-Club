from django.shortcuts import render


def home(request):
    return render(request, "events/events.html")


def leaderboard(request):
    return render(request, "events/leaderboard.html")


def apply(request):
    return render(request, "events/apply.html")
