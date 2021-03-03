from django.shortcuts import render
from board.models import Categorys
from board.models import Threads
# from board.models import Messages


def index(request):
    categorys = Categorys.objects.all()
    data = {'categorys': categorys}
    return render(request, template_name='categorys.html', context=data)


def threads_view(request, name):
    name = Categorys.objects.get(category=name)
    threads = Threads.objects.filter(category=name)
    data = {'threads': threads, 'name': name}
    return render(request, template_name='threads.html', context=data)


def thread_view(request, name, thread):
    data = {}
    # data = {'messages': messages}
    return render(request, template_name='thread.html', context=data)
