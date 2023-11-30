from django.contrib import admin

# Register your models here.
from .models import Tag, TodoList


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ('name',)

   
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ('due_date',)
