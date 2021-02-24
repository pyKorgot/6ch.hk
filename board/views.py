from django.shortcuts import render
from board import forms
from board.models import Threads, Categorys


def main(request):
    data = {'categors': Categorys.objects.all()}
    return render(request, 'main.html', context=data)


def index(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        Threads.objects.create(messages=message)
    threads = Threads.objects.all()
    data = {'threads': threads, 'form': forms.MessageForms}
    return render(request, 'thread.html', context=data)
