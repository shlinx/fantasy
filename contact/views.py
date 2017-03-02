from django.shortcuts import render


def index(request):
    return render(request, 'contact/contact.html')


def submit(request):

    pass
