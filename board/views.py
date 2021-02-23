from django.shortcuts import render
from board import forms
from board.models import Thread


def index(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        Thread.objects.create(messages=message)
    threads = Thread.objects.all()
    data = {'threads': threads, 'form': forms.MessageForms}
    return render(request, 'thread.html', context=data)
