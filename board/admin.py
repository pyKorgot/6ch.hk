from django.contrib import admin
from board.models import Threads, Categorys, Messages


class CategorysAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


class ThreadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('thread', 'published', 'message',)


admin.site.register(Threads, ThreadsAdmin)
admin.site.register(Categorys, CategorysAdmin)
admin.site.register(Messages, MessagesAdmin)
