from django.shortcuts import render


def register(request):
    return render(request, 'register.html')


def reports(request):
    return render(request, 'reports.html')
