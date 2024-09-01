# from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    # return HttpResponse('Hello, World! This is the homepage of myProject.')
    return render(request, 'home.html')


def aboutPage(request):
    # return HttpResponse('This is the about page of myProject.')
    return render(request, 'about.html')
