from django.contrib import admin
from board.models import Threads, Categorys, Messages


admin.site.register(Threads)
admin.site.register(Categorys)
admin.site.register(Messages)
