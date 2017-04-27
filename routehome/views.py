from django.shortcuts import render
# Create your views here.


def code(request):
    return render(request, './pages/code.html')


def team(request):
    return render(request, './pages/team.html')


def about(request):
    return render(request, './pages/about.html')


def readme(request):
    return render(request, './pages/readme.html')
