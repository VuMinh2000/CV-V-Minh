from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        messages.success(request, "Message sent successfully!!!")
        return HttpResponseRedirect('/')

