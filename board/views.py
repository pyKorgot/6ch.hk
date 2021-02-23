from django.shortcuts import render
from board import forms


def index(request):
    return render(request, 'thread.html', {'form': forms.MessageForms})
