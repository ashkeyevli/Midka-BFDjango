from django.contrib import admin

# Register your models here.
from django.contrib import admin
from books.models import BookJournalBase, Book, Journal
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'created_at', 'num_pages', 'genre']
    ordering = ['id']


@admin.register(Journal)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'created_at', 'type', 'publisher']
    ordering = ['id']
