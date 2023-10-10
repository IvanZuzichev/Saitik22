from django.shortcuts import render
from django.http import HttpResponse

def starts(request):
    return render(request, 'startpage.html')
def apis(request):
    return render(request, 'apishka.html')
def users(request):
    return render(request, 'user.html')
def trashs(request):
    return render(request, 'trash.html')
def check(request):
    return HttpResponse('<h1>qwert</h1>')

