from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'author', 'isbn', 'price')
    search_fields = ('title', 'subtitle', 'author', 'isbn', 'price')
    list_filter = ('title', 'subtitle', 'author', 'isbn', 'price')


admin.site.register(Book, BookAdmin)
admin.site.site_header = "Library Management System"
admin.site.site_title = "Library Management System"
admin.site.index_title = "Welcome to Library Management System"
